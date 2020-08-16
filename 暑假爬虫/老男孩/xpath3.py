import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/83.0.4103.116 Safari/537.36" }
    page_text = requests.get(url = url, headers = headers).text
    tree = etree.HTML(page_text)

    # li_list = tree.xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/ul/li')
    # for li in li_list:
    #     hot_name = li.xpath('./a/text()')[0]
    #     # print(hot_name)
    #
    # ul_list = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul')
    # for ul in ul_list:
    #     print(ul.xpath('./div/b/text()')[0])
    #     ul_li_list = ul.xpath('./div/li')
    #     for ul_li in ul_li_list:
    #         all_name = ul_li.xpath('./a/text()')[0]
    #         print(all_name)

    hot_xpath = '/html/body/div[3]/div/div[1]/div[1]/div[2]/ul/li/a'
    all_xpath = '/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]/li/a'
    a_list = tree.xpath(hot_xpath + '|' + all_xpath)
    for a in a_list:
        city = a.xpath('./text()')[0]
        print(city)
