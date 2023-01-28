from requests import get            # pip3 install requests
from bs4 import BeautifulSoup       # pip3 install beautifulsoup4

def convert_job_data(job_post):
    company, type, region = job_post.find_all("span", class_="company")     # list의 인덱스 순서대로 각 변수에 값이 할당됨
    title = job_post.find("span", class_="title")
    anchors = job_post.find_all("a")
    anchor = anchors[1]
    link = anchor["href"]   # BeautifulSoup이 dictionary로 만들어주므로 anchor["href"] 이렇게 사용 가능
    job_data = {
        'link': f"https://weworkremotely.com{link}",
        'company': company.string,
        'type': type.string,
        'location': region.string,
        'position': title.string
    }
    return job_data


def extract_wwr_jobs(keyword):
    url = "https://weworkremotely.com/remote-jobs/search?term="

    response = get(f"{url}{keyword}")
    results = []

    if response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        for section in jobs:
            job_posts = section.find_all("li")
            job_posts.pop(-1)
            for job_post in job_posts:
                results.append(convert_job_data(job_post))
    return results
