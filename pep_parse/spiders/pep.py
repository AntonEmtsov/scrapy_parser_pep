import re
import scrapy

from pep_parse.settings import PATTERN
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep in response.css(
            'section#numerical-index td a::attr(href)'
        ).getall():
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = re.search(
            PATTERN,
            ''.join(response.css('h1.page-title::text').getall()),
        ).groups()
        yield PepParseItem(
            {
                'number': number,
                'name': name,
                'status': response.css(
                    'dt:contains("Status") + dd abbr::text'
                ).get(),
            }
        )
