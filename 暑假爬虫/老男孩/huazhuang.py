import json

import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/83.0.4103.116 Safari/537.36" }
# 存放所有企业ID
id_list = []
# 存放所有具体信息
detail_list = []
# 首页的url
url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
# 每个企业的url
post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'


def get_id(lo, hi):
    for page in range(lo, hi):
        page = str(page)
        data = {
            'on':'true',
            'page':page,
            'pageSize':'15',
            'productName':'',
            'conditionType':'1',
            'applyname':'',
            'applysn':'',
        }
        json_ids = requests.post(url = url, headers = headers, data = data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
        return id_list


def get_detail(ids):
    for id_com in ids:
        data = { 'id':id_com }
        detail_json = requests.post(url = post_url, headers = headers, data = data).json()
        detail_list.append(detail_json)
    return detail_list


if __name__ == '__main__':

    # for page in range(1, 6):
    #     page = str(page)
    #     data = {
    #         'on':'true',
    #         'page':page,
    #         'pageSize':'15',
    #         'productName':'',
    #         'conditionType':'1',
    #         'applyname':'',
    #         'applysn':'',
    #     }
    #     json_ids = requests.post(url = url, headers = headers, data = data).json()
    #     for dic in json_ids['list']:
    #         id_list.append(dic['ID'])

    # for id in id_list:
    #     data = { 'id':id }
    #     detail_json = requests.post(url = post_url, headers = headers, data = data).json()
    #     detail_list.append(detail_json)

    ids = get_id(2, 5)

    details = get_detail(ids)

    with open('./huazhuang.json', 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(details, indent = 2, ensure_ascii = False))
    print('over!')
