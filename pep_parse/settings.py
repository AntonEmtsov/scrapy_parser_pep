from pathlib import Path
from datetime import datetime as dt


BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

BASE_DIR = Path(__file__).parent.parent
DATA_FORMAT = dt.now().strftime('%Y-%m-%dT%H-%M-%S')
PEPS_FILE_NAME = '{results}/pep_%(time)s.csv'
RESULTS = 'results'
STATUS_SUMMARY_FILE_NAME = 'status_summary_{DATA_FORMAT}.csv'


FEEDS = {
    PEPS_FILE_NAME.format(results=RESULTS): {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}

PATTERN = r'^PEP\s(?P<number>\d+)[\s–]+(?P<name>.*)'
