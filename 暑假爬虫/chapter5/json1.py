import json

string = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
# # 1. loads 将字符串转换为对象(可操作)
# # print(type(string))
# data = json.loads(string)
# print(data)
# print(data[0].get('name'))
# # print(type(data))

# # 2. 先从文件读取字符串再转换为对象
# with open('data.json', 'r') as f:
#     s = f.read()
#     data = json.loads(s)
#     print(data)


# # 3. 写入json
# data = [{
#     'name':'Bob',
#     'gender':'male',
#     'birthday':'1992-10-18'
# }]


# 3.1 不带中文的写法
# with open('data.json', 'w') as file:
#     file.write(json.dumps(data, indent = 2))

# 3.2 带中文的写法
# with open('data.json', 'w', encoding = 'utf-8') as file:
#     file.write(json.dumps(data, indent = 2, ensure_ascii = False))
