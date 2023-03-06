import csv
from collections import defaultdict

from pep_parse.settings import (
    BASE_DIR,
    DATA_FORMAT,
    RESULTS,
    STATUS_SUMMARY_FILE_NAME,
)


class PepParsePipeline:

    def open_spider(self, spider):
        self.result = defaultdict(int)

    def process_item(self, item, spider):
        self.result[item['status']] += 1
        return item

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def close_spider(self, spider):
        file_name = (
            self.results_dir / STATUS_SUMMARY_FILE_NAME.format(
                DATA_FORMAT=DATA_FORMAT,
            )
        )
        with open(file_name, mode='w', encoding='utf-8') as file:
            csv.writer(
                file,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE,
            ).writerows(
                (
                    ('Статус', 'Колличество'),
                    *sorted(self.result.items()),
                    ('Всего', sum(self.result.values())),
                )
            )
