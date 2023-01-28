from extractors.indeed import extract_indeed_job
from extractors.wwr import extract_wwr_jobs

search_keyword = input("What do you want to search for?")

file = open(f"{search_keyword}.csv", "w")
file.write("Position,Company,Location,URL\n")


wwr = extract_wwr_jobs(search_keyword)
indeed = extract_indeed_job(search_keyword)

all_jobs = wwr + indeed

for job in all_jobs:
    file.write(f"{job['position'].replace(',', ' ')},{job['company'].replace(',', ' ')},{job['location'].replace(',', ' ')},{job['link'].replace(',', ' ')}\n")

file.close()

# print(all_jobs)


