# ForGraduation
I hope to graduate smoothly ︿(￣︶￣)︿
这个是爬虫测试，爬取得是一个网站的文章标题，内容，日期，点赞数等
框架是scrapy 这个框架很简单，但是环境有点复杂，依赖比较多，不过都很小
Python环境是3.5
代码还有一点没改玩，时间和Mysql数据库导入还有一点点问题

你可以先学scrapy框架，里面主要是学习正则表达式和xpath语法，其他的都很简单，我明天添加注释

这个看完之后，我们就可以开始爬取目标网站了

代码结构分析：
工程结构主体是由scrapy自动创建的
1 主程序 Article/Article/spiders/jobble.py
2 文章内容对象及一些处理函数 Article/Article/items.py
3 数据库保存、图片下载等处理函数 Article/Article/pipleline.py
4 配置文件，包含数据库地址等常数参量与3中处理函数的配置 Article/Article/settings.py

你想配置环境的话，就先按照python，然后直接用pip 安装scrapy，如果缺依赖，就再下就好