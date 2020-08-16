import requests
import logging

# 1. post 上传文件

# files = { 'file':open('favicon.ico', 'rb') }
# r = requests.post('http://httpbin.org/post', files = files)
# print(r.text)

# 2. cookies

# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)

# 3. 维持同一个会话

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# 4. SSL证书

# # 捕获警告到日志
# logging.captureWarnings(True)
# r = requests.get('https://www.12306.cn', verify = False)
# print(r.status_code)

# 5. 代理设置

# proxies = {
#     'http':'http://user:password@10.10.1.10:3128/',
# }
# requests.get('https://www.taobao.com', proxies = proxies)

# 6. 超时设置

# r = requests.get('https://www.taobao.com', timeout = 1)  # 1s
# r = requests.get('https://www.taobao.com', timeout = None)  # 默认, 没有时间限制


