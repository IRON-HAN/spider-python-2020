import requests
from lxml import etree
import os

if __name__ == '__main__':

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/83.0.4103.116 Safari/537.36" }
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    # url = 'http://pic.netbian.com/4kmeinv/'
    for page in range(2, 4):
        url = 'http://pic.netbian.com/4kmeinv/index_%d.html' % page
        page_text = requests.get(url = url, headers = headers).text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]/ul/li')
        for li in li_list:
            img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
            # 处理中文乱码
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            img_data = requests.get(url = img_src, headers = headers).content
            img_path = 'picLibs/' + img_name
            with open(img_path, 'wb') as f:
                f.write(img_data)
                print(img_name + '下载成功')
