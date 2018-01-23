import scrapy
from scrapy.spiders import crawl


class QuotesSpider(scrapy.Spider):
    name = "aso100"
    start_urls = [
        'http://vipheyue.oss-cn-hangzhou.aliyuncs.com/temporaryAPK/file1.html',
    ]

    def parse(self, response):
        index = 1

        with open('/Users/heyue/Downloads/quotesbot-master/quotesbot/files/str.txt', 'a') as f:
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
