# baike_spider
爬百度百科相关文章的标题与摘要
感觉教程很好，思路清晰明确，给老师点赞～

## 教程地址
慕课网：https://www.imooc.com/video/10695?_blank

## 爬虫流程
![](http://www.lypeng.com/uploads/image/5b166ea0db5d2.jpg)

## 以下三个为测试文件不用理
1. mysoup.py
2. myspider.py
3. html.txt

## 问题简单说明
1. html_downloader.py下载那里，没有用urllib，使用requests代替，感觉更熟悉与方便
2. html_outputer.py里面不需要对data['title']转码，添加.encode('utf-8')后，反而乱码，变成二进制了
3. html_parser.py里面，去掉soup = BeautifulSoup(html_cont, 'html.parser')最后的编码from-encoding='utf-8',否则报错
4. spider_main.py 开始测试可以写个5或者10，测试结束后，可以改为1000

## 代码执行效果图
![](http://www.lypeng.com/uploads/image/5b1672d75d146.jpg)

## git地址
https://github.com/lypeng29/baike_spider.git?_blank

## 效果预览
http://t.dpshop.net/python/baike_spider/output.html?_blank




