import requests
from bs4 import BeautifulSoup

KEYWORD = "파이썬"
DOMAIN = "http://www.jobkorea.co.kr"
REQUEST_URL = f'http://www.jobkorea.co.kr/Search/?stext={KEYWORD}&tabType=recruit'
result = []


def get_list(last_page):
    data = []
    for i in range(1, last_page+1):
        response = requests.get(f"{REQUEST_URL}&Page_No={i}")
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        list_items = soup.select('li[class=list-post]')
        data.extend(extract_job_data(list_items))
        if i == 20:
            break
    return data


def extract_job_data(html):
    LIMIT = 20
    result = []
    for i in range(0, LIMIT):
        company_name = html[i].find('a').text
        title = html[i].find(
            'div', {"class": "post-list-info"}).find('a')["title"]
        link = html[i].find(
            'div', {"class": "post-list-info"}).find('a')["href"]
        info = {
            "company": company_name,
            "title": title,
            "link": DOMAIN+link
        }
        result.append(info)
    return result
