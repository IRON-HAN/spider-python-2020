import requests
from bs4 import BeautifulSoup
import re
import random
import time
import parsel

base_url = "https://baike.baidu.com"
history = ["/item/Python/407313"]
for i in range(20):
    url = base_url + history[-1]
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/83.0.4103.116 Safari/537.36" }
    time.sleep(3)
    html = requests.get(url = url, headers = header).text
    soup = BeautifulSoup(html, features = 'lxml')
    print(soup.find('h1').get_text())

    sub_urls = soup.find_all("a",
                            {"target":"_blank", "href" : re.compile('/item/(%.{2})+$')})
    if len(sub_urls) != 0:
        history.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        history.pop()
    print(history)
