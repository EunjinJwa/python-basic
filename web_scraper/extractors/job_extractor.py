from extractors.indeed import extract_indeed_job
from extractors.wwr import extract_wwr_jobs
from extractors.jobkorea import extract_jobkorea_jobs
from database.db_memory import add, get, exists_keyword

def extract_job(keyword):
    jobs = []
    if exists_keyword(keyword):
        jobs = get(keyword)
    else:
        wanted = extract_jobkorea_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        # indeed = extract_indeed_job(keywork)

        jobs = wanted + wwr
        add(keyword, jobs)
    return jobs