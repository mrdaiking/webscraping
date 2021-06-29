import time

from bs4 import BeautifulSoup

# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#
#     soup = BeautifulSoup(content, 'lxml')
#     # print(soup.prettify())
#     # tags = soup.find_all('h5')
#     # courses_html_tags = soup.find_all('h5')
#     # for course in courses_html_tags:
#     #     print(course.text)
#     course_card = soup.find_all('div', class_='card')
#     for course in course_card:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1] #loai bo khoang trang va tao mang, -1 la phan tu cuoi cung
#
#         print(course_name)
#         print(course_price)
    # print(tags)

import requests


print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More info: {more_info} \n")
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Watiing {time_wait} seconds...')
        time.sleep(600)


