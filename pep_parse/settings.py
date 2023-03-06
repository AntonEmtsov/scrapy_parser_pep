from pathlib import Path


BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
ROBOTSTXT_OBEY = True
URL = 'peps.python.org'

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

BASE_DIR = Path(__file__).parent.parent
DATE_FORMAT = '%Y-%m-%dT%H-%M-%S'
STATUS_SUMMARY_FILE_NAME = 'status_summary_{date}.csv'
RESULTS = 'results'

FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}

PATTERN = r'^PEP\s(?P<number>\d+)[\s–]+(?P<name>.*)'
