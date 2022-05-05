print("Hello, Here is a list of Junior Software Engineer jobs in the Atlanta area:")
from bs4 import BeautifulSoup

import requests
import time
def find_jobs():
        html_text = requests.get("https://www.linkedin.com/jobs/search?keywords=%22junior%20software%20engineer%22&location=Atlanta%2C%20Georgia%2C%20United%20States&geoId=106224388&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0").text
        soup = BeautifulSoup(html_text, "lxml")
        jobs = soup.find_all("div", class_ = "base-card base-card--link base-search-card base-search-card--link job-search-card")

        for job in jobs:

            published_data = job.find("time", class_ = "job-search-card__listdate")
            if "days" or "weeks" in published_data:
                job_name = job.find("h3", class_= "base-search-card__title").text.replace(' ','')
                company = job.find("h4", class_= "base-search-card__subtitle").text.replace(' ','')
                company_name = job.h4.text.replace(' ','')
                more_info = soup.div.h4.a["href"]
                #print(f'''Company Name:{company_name}Job Title:{job_name}''') --- THIS IS A LONG VIEW TO PRINT JOB POSTING

                #below is the same result in a tight view
                print(f"Company Name:{company_name.strip()}") #.strip() is used to close any white space in string
                print(f"Job Title:{job_name.strip()}")
                print(f"More Info:{more_info}")
                print('')
while True:
    find_jobs()
    time_wait = 60 #minutes
    print(f"Waiting {time_wait} minutes...")
    time.sleep(time_wait * 60) #seconds