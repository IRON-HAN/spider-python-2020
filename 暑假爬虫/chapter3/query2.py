# 1. 基本的CSS选择器

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq

doc = pq(html)

# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

items = doc('.list')
print(items)

# lis = items.find('li')
# print(lis)


# # 2. 单个节点的打印
# li = doc('.item-0.active')
# print(li)

# # 3. 多个节点进行遍历
# lis = doc('li').items()
# for l in lis:
#     print(l)

# 4. 获取单个属性值
# a = doc('.item-0.active a')
# print(a)
# print(a.attr('href'))
# # 与下面语句等价
# print(a.attr.href)

# # 5. 获取多个属性值
# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))

# # 6. 获取文本
# a = doc('.item-0.active a')
# print(a.text())

# # 7. 获取节点内部的HTML文本
# li = doc('.item-0.active')
# print(li)
# print(li.html())
