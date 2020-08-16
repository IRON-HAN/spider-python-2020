from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/83.0.4103.116 Safari/537.36" }
    fp = open('./sanguo.txt', 'w', encoding = 'utf-8')
    for cnt in range(1, 10):
        # 1 url
        url = 'https://www.shicimingju.com/book/sanguoyanyi/%d.html' % cnt
        # 2 解析
        page_text = requests.get(url = url, headers = headers).text
        # 3 soup
        soup = BeautifulSoup(page_text, 'lxml')
        # 定位标题的tag
        title_tag = soup.find('h1')
        # 标题内容
        title = title_tag.text
        # 具体tag
        detail_tag = soup.find('div', class_ = 'chapter_content')
        # 具体内容
        detail = detail_tag.text
        fp.write(title + '\n' + detail + '\n')
        print(title + '\t爬取成功!')
    fp.close()
