def save_to_file(keyword, jobs):
    file = open(f"{keyword}.csv", "w")
    file.write("Position,Company,Location,URL\n")
    for job in jobs:
        file.write(f"{job['position'].replace(',', ' ')},{job['company'].replace(',', ' ')},{job['location'].replace(',', ' ')},{job['link'].replace(',', ' ')}\n")
    file.close()