import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import (
    BASE_DIR,
    DATE_FORMAT,
    RESULTS,
    STATUS_SUMMARY_FILE_NAME,
)


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def close_spider(self, spider):
        with open(self.results_dir / STATUS_SUMMARY_FILE_NAME.format(
            date=dt.now().strftime(DATE_FORMAT)),
            mode='w',
            encoding='utf-8',
        ) as file:
            csv.writer(
                file,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE,
            ).writerows((
                ('Статус', 'Колличество'),
                *sorted(self.results.items()),
                ('Всего', sum(self.results.values())),
            ))
