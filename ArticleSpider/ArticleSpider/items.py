# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
import datetime
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticleItemLoader(ItemLoader):
    # 自定义itemloader,这是由于原有的loader会返回一个list，而我们只要其中的数值,也就是列表第一个元素
    default_output_processor = TakeFirst()


def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date


def return_value(value):
    return value


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


# def concat_tags(value):
#     res = ""
#     for tag in value:
#         if "评论" not in tag:
#             if res == "":
#                 res = tag
#             else:
#                 res = res + ","+str(tag)
#
#     return res


class JobboleArticleItem(scrapy.Item):
    title = scrapy.Field()
    front_image_path = scrapy.Field()
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert)
    )
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    tags = scrapy.Field()
    contents = scrapy.Field()
    likeNum = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )

    def get_insert_sql(self):
        insert_sql = """
            insert into article(title, url_obj_id, content, tags, like_num, front_img_path,
            create_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (self["title"], self["url_object_id"], self["contents"], self["tags"], self["likeNum"],
                  self["front_image_path"], self["create_date"])
        return insert_sql, params


