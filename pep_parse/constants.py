from pathlib import Path
from datetime import datetime as dt

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
DATA_FORMAT = dt.now().strftime('%Y-%m-%dT%H-%M-%S')
STATUS_SUMMARY_FILE_NAME = 'status_summary_{DATA_FORMAT}.csv'

PATTERN = r'^PEP\s(?P<number>\d+)[\s–]+(?P<name>.*)'
