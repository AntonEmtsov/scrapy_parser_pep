import csv
from collections import defaultdict

from pep_parse.constants import (
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

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS  # тесты
        results_dir.mkdir(exist_ok=True)
        file_name = (
            results_dir / STATUS_SUMMARY_FILE_NAME.format(
                DATA_FORMAT=DATA_FORMAT,
            )
        )
        with open(file_name, mode='w', encoding='utf-8') as file:
            csv.writer(
                file,
                dialect=csv.unix_dialect,
            ).writerows(
                (
                    ('Статус', 'Колличество'),
                    *sorted(self.result.items()),
                    ('Всего', sum(self.result.values())),
                )
            )
