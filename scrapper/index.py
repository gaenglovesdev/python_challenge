import requests
from bs4 import BeautifulSoup
from extract_data import get_list
from save_data import save_to_file

KEYWORD = "파이썬"
response = requests.get(
    f'http://www.jobkorea.co.kr/Search/?stext={KEYWORD}')

html = response.text
soup = BeautifulSoup(html, 'html.parser')

last_page = int(soup.select('span[class=pgTotal]')[0].text)

data = get_list(last_page)

save_to_file(data)
