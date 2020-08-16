from pyquery import PyQuery as pq
import requests


# 1. 可以通过url初始化
doc = pq(url = 'https://cuiqingcai.com')
# 等价于下面的语句
# doc=pq(requests.get('https://cuiqingcai.com').text)
print(doc('title'))

#  2. 通过本地html文件初始化