
from requests import get            # pip3 install requests
from bs4 import BeautifulSoup       # pip3 install beautifulsoup4
from extractors.wwr import extract_wwr_jobs

results = extract_wwr_jobs("python")
print(results)






