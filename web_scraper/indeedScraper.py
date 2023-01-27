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

results = []
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        info = job.select_one("h2 a")
        link = info['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        position = info['aria-label']
        
        job_data = {
            'link': f"https://kr.indeed.com{link}",
            'company': company.string,
            'location': location.string,
            'position': position
        }
        results.append(job_data)

for result in results:
    print(result)


