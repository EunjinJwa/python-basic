from extractors.indeed import extract_indeed_job
from extractors.wwr import extract_wwr_jobs

db = {}

def extract_job(keyword):
    jobs = []
    if keyword in db:
        jobs = db[keyword]
    else:
        wwr = extract_wwr_jobs(keyword)
        # indeed = extract_indeed_job(keywork)
        jobs = wwr
        db[keyword] = jobs
    return jobs