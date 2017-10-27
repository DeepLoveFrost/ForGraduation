# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ArticleSpider.items import JobboleArticleItem, ArticleItemLoader
from ArticleSpider.utils.common import get_md5


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        lists = response.xpath("//div[@class='post floated-thumb']/div[@class='post-thumb']/a")
        for item in lists:
            url = item.xpath("./@href").extract_first()
            img_url = item.xpath("./img/@src").extract_first()
            yield Request(url=url, meta={"front_image_url": img_url}, callback=self.parse_detail)

        # next_url = response.xpath("//a[@class='next page-numbers']/@href").extract()
        # # if next_url:
        # #     yield Request(url=next_url, callback=self.parse)
        # # pass

    def parse_detail(self, response):
        front_img_url = response.meta["front_image_url"]
        item_loader = ArticleItemLoader(item=JobboleArticleItem(), response=response)
        item_loader.add_xpath("title", "//div[@class='entry-header']/h1/text()")
        item_loader.add_xpath("tags", "//p[@class='entry-meta-hide-on-mobile']/a/text()")
        item_loader.add_xpath("contents", "//div[@class='entry']")
        item_loader.add_xpath("likeNum", "//span[contains(@class,'vote-post-up')]/h10/text()")
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_value("front_image_url", [front_img_url])
        item_loader.add_xpath("create_date", "//p[@class='entry-meta-hide-on-mobile']/text()")

        article_item = item_loader.load_item()
        yield article_item
