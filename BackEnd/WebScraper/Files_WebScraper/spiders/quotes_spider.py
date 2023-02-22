import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'AR/VR'

    start_urls = ['https://clutch.co/developers/virtual-reality']

    def parse(self, response):
        company_page_links = response.css('.data-title + a')
        yield from response.follow_all(company_page_links, self.parse_aut)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'AR/VR Company': extract_with_css('h3.data-title::text'),
        }