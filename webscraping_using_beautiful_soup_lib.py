from bs4 import BeautifulSoup
import requests
import time
def find_job():

    print('unfamiliar skills')
    unfimiliar_skills = input('Enter unfamiliar skills separated by commas: ').split(',')
    print('result without the unfamiliar skills')
    response=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
    #print(response)
    soup=BeautifulSoup(response.text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').text.replace('','')

        if 'few' in published_date:
            job_title=job.find('h2').text.replace('','')
            company_name=job.find('h3').text.replace('','')
            skills=job.find('div',class_='srp-skills').text.replace('','')
            more_info=job.header.h2.a['href']
            if not any(skill.strip() in skills for skill in unfimiliar_skills):
                with open(f'posts/{index}.txt','w') as f:

                    f.write(f'Job Title: {job_title.strip()}')
                    f.write(f'Company Name: {company_name.strip()}')
                    f.write(f'Skills: {skills.strip()}')
                    f.write(f'More Info: {more_info.strip()}')

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60) # 10 minutes
