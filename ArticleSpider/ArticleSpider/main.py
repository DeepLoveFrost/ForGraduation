# -*- coding: utf-8 -*-
_author_ = 'tao'
from scrapy.cmdline import execute
import sys
import os

# os.path.abspath(__file__) 该文件的路径
# os.path.dirname 父目录
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole"])

# import re
#
# # value = '     2017/10/19  .'
# # match_re = re.match(".*?(\d+/\d+/\d+).*", value)
# # if match_re:
# #    print(match_re.group(1))
