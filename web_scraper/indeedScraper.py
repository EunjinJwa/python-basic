from requests import get            # pip3 install requests
from bs4 import BeautifulSoup       # pip3 install beautifulsoup4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


base_url = "https://kr.indeed.com/jobs?q="
search_keyword = "java"

browser = webdriver.Chrome(options=options)

browser.get(f"{base_url}{search_keyword}")
response = browser.page_source

soup = BeautifulSoup(response, "html.parser")
jobs = soup.find("ul", class_="jobsearch-ResultsList").find_all("li", recursive=False)
for job in jobs:
    print(job)
    print("=====================")


