import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import HTTPS_URL, PATTERN, URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [URL]
    start_urls = [HTTPS_URL.format(url=URL)]
    # start_urls = [f'https://{URL}/']

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
        yield PepParseItem(dict(
            number=number,
            name=name,
            status=response.css('dt:contains("Status") + dd abbr::text').get(),
        ))
