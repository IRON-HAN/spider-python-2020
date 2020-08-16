import requests
import parsel
import time

page_num = 0
for page in range(50, 1000 + 1, 50):
    page_num += 1
    print('正在爬取第{}页'.format(page_num))

    # 1. url
    url = 'https://tieba.baidu.com/f?kw=%E7%BA%A6%E4%BC%9A&ie=utf-8&pn={}'.format(str(page))
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko " }

    # 2. 发送请求
    response = requests.get(url = url, headers = header)
    html_data = response.text

    # 3. 解析数据(两层数据解析)
    html = parsel.Selector(html_data)
    title_url = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href').getall()
    second_url = 'https://tieba.baidu.com'
    for u in title_url:
        all_url = second_url + u
        print('当前链接为', all_url)

        response_2 = requests.get(url = all_url, headers = header).text
        response_2_data = parsel.Selector(response_2)
        result_list = response_2_data.xpath('//cc/div/img[@class="BDE_Image"]/@src').getall()

        for li in result_list:
            time.sleep(1)
            img_data = requests.get(url = li, headers = header).content

            file_name = li.split('/')[-1]
            with open('img\\' + file_name, mode = 'wb') as f:
                f.write(img_data)
                print('正在保存', file_name)
