import scrapy


class RecruitSpider(scrapy.spiders.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        item = Doubantop250Item()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMovie in Movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = "".join(title)
            movieInfo = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle
            item['movie'] = ';'.join(movieInfo)
            item['star'] = star
            item['quote'] = quote
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            yield Request(urljoin(response.url, nextLink), callback=self.parse)
