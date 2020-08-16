import requests

# 1. 使用get请求+参数

# data = {
#     'name':'ger',
#     'age':22
# }
# r = requests.get('http://httpbin.org/get', params = data)
# print(r.text)
# print(r.json())

# 2. 爬取二进制数据

# r = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# 3. 使用post请求

# data={'name': 'ger', 'age': 22}
# r=requests.post('http://httpbin.org/post', data = data)
# print(r.text)


