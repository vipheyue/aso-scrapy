import scrapy
from scrapy.spiders import crawl


class QuotesSpider(scrapy.Spider):
    name = "aso100doutu"
    start_urls = [
        'http://vipheyue.oss-cn-hangzhou.aliyuncs.com/temporaryAPK/jisuanqi2.html',
    ]

    def parse(self, response):
        index = 1
        mytxt='/Users/heyue/Documents/Work/pythonSpace/aso-scrapy/quotesbot/files/jisuanqi2.txt'
        with open(mytxt, 'w') as b:
            b.close()
        with open(mytxt, 'a') as f:
            for item in response.css("div.ivu-table-cell"):
                mul = index % 6
                print("index:    "+str(index)+"     mul:  "+str(mul))
                textcontent = item.css("a::text").extract_first()
                index = index + 1
                if (mul == 3):
                    print(".........." * 20)
                    print(textcontent)
                    f.write(str(textcontent)+'\n')
                    pass
