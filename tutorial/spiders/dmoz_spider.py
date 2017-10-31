import scrapy
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
t1 = []
tag = "javascript"

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["https://stackoverflow.com/questions/178325/how-do-i-check-if-an-element-is-hidden-in-jquery?page=1&tab=votes#tab-top"]
    """
    for i in range(1,20):
        temp_urls = "https://stackoverflow.com/questions/tagged/"+tag+"?page="+str(i)+"&sort=votes&pagesize=50"
        start_urls.append(temp_urls)
    """
    def parse(self, response):
        
        global t1
        t = response.xpath('//td[@class="post-signature owner"]/div[@class="user-info "]/div[@class="user-details"]/a/text()').extract()
        t1 += response.xpath('//div[@class="user-details"]/a/text()').extract()
        
        print ", ".join(t)
        print (", ".join(t1)).encode('utf-8')
        
        
        filename = tag
        with open(filename,'wb') as f:
            f.write(", ".join(t1))
        