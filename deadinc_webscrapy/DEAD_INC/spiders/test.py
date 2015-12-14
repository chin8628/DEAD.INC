import scrapy
from download_file import *
from country_data import country_data_func

cnt = 1

class DmozSpider(scrapy.Spider):

    data = country_data_func()
    #data = {"Thailand": "http://data.worldbank.org/country/thailand"}
    list_url = list()
    for i in sorted(data):
	list_url.append(data[i])

    name = "DEAD_INC"
    start_urls = list_url

    def parse(self, response):

	global cnt

	for sel in response.xpath('//*[@id="data-browser"]/ul/li[2]/span/ul/li[2]'):
            link =  sel.xpath('a/@href').extract()
            print "Order:", cnt, "Downloading...", link[0]
            download_file(link[0])

	cnt += 1
    
