import requests
from bs4 import BeautifulSoup
import time

start_time = time.time()
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://dictionary.cambridge.org/',
    'Connection': 'keep-alive',
}
input_word = input("Please input your word: ")


def trans_me(keyword):
    response = requests.get('https://dictionary.cambridge.org/us/dictionary/english/' + keyword, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    word = soup.find('span', class_='hw dhw')
    type = soup.find('span', class_='pos dpos')
    ipa = soup.find('span', class_='ipa dipa lpr-2 lpl-1')
    print(f'Word: {word.text}')
    print(f'Type: {type.text}')
    print(f'IPA: /{ipa.text}/')
    means = soup.find_all('div', class_='def ddef_d db')
    for mean in means:
        mean = mean.text.replace(':', '')
        print(f'Mean: {mean}')


trans_me(input_word)
print("Response in --- %s seconds ---" % (time.time() - start_time))
