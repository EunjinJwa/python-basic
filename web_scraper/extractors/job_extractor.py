from extractors.indeed import extract_indeed_job
from extractors.wwr import extract_wwr_jobs
from database.db_memory import add, get, exists_keyword

def extract_job(keyword):
    jobs = []
    if exists_keyword(keyword):
        jobs = get(keyword)
    else:
        wwr = extract_wwr_jobs(keyword)
        # indeed = extract_indeed_job(keywork)
        jobs = wwr
        add(keyword, jobs)
    return jobs