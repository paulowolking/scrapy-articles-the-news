import scrapy

from notices_the_news.items import NoticeItem


class NoticesSpider(scrapy.Spider):
    name = "notices"
    start_urls = [
        'https://thenewscc.com.br/noticias/',
    ]

    def parse(self, response):
        articles = response.xpath('//div[@class="elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-9a761cc"]//article')
        for article in articles:
            texts = article.xpath('././/div[@class="elementor-post__text"]//p//span//text()').getall()
            text_replace = [text.replace('\xa0',' ') for text in texts]
            noticeItem = NoticeItem()
            noticeItem['image_url'] = article.xpath('././/div[@class="elementor-post__thumbnail"]//@data-large-file').get()
            noticeItem['notice_link'] = article.xpath('././/a[@class="elementor-post__thumbnail__link"]//@href').get()
            noticeItem['title'] = article.xpath('././/h2[@class="elementor-post__title"]//a//text()').get().strip()
            noticeItem['data'] = article.xpath('././/span[@class="elementor-post-date"]//text()').get().strip()
            noticeItem['texts_replace'] = ''.join(text_replace)
            
            yield noticeItem
            # yield{
            #     'image_url': article.xpath('././/div[@class="elementor-post__thumbnail"]//@data-large-file').get(),
            #     'notice_link': article.xpath('././/a[@class="elementor-post__thumbnail__link"]//@href').get(),
            #     'title': article.xpath('././/h2[@class="elementor-post__title"]//a//text()').get().strip(),
            #     'data': article.xpath('././/span[@class="elementor-post-date"]//text()').get().strip(),
            #     'texts_replace': ''.join(text_replace),
            # }
            