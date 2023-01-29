from requests import get            # pip3 install requests
from bs4 import BeautifulSoup       # pip3 install beautifulsoup4

base_url = "https://www.jobkorea.co.kr"

def convert_job_data(job_post):
    company = job_post.find("div", class_="post-list-corp").find("a")['title']
    detail = job_post.find("div", class_="post-list-info", recursive=True)

    title = detail.find("a")['title']
    location = detail.find("span", class_="loc long")
    link = detail.find("a")['href']

    job_data = {
        'link': f"{base_url}{link}",
        'company': company,
        'location': location.string,
        'position': title
    }

    return job_data

        
def extract_jobkorea_jobs(keyword):
    url = f"{base_url}/Search/?stext="

    response = get(f"{url}{keyword}")
    results = []

    if response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find("div", class_="list-default")
         
        job_posts = jobs.find_all("li", class_="list-post")
        for job_post in job_posts:
            results.append(convert_job_data(job_post))
    return results


def extract_wanted_all():
    url = "https://www.jobkorea.co.kr/Search/?stext=test"

    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("div", class_="lists-cnt")
    
    print(cards)

# extract_wanted_all()
extract_jobkorea_jobs('python')