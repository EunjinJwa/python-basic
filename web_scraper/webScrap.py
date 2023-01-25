
from requests import get
from bs4 import BeautifulSoup


def convert_job_data(job_post):
    company, type, region = job_post.find_all("span", class_="company")
    title = job_post.find("span", class_="title")
    job_data = {
        'company': company.string,
        'type': type.string,
        'region': region.string,
        'title': title.string
    }
    return job_data



print("Run")

url = "https://weworkremotely.com/remote-jobs/search?term="
search_keyword="java"

response = get(f"{url}{search_keyword}")
job_boards = []

if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("section", class_="jobs")
    for section in jobs:
        job_posts = section.find_all("li")
        job_posts.pop(-1)
        for job_post in job_posts:
            job_boards.append(convert_job_data(job_post))
print(job_boards)
print("good!")

