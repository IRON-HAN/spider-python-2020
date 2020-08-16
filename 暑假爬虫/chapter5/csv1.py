import csv

# # 1. 写入行
# with open('data.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ')
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', 20])
#     writer.writerow(['10002', 'Bob', 22])
#     writer.writerow(['10003', 'Jordan', 21])

# # 2. 写入字典
# with open('data.csv', 'w') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
#     writer.writeheader()
#     writer.writerow({ 'id':'10001', 'name':'Mike', 'age':20 })
#     writer.writerow({ 'id':'10002', 'name':'Bob', 'age':22 })
#     writer.writerow({ 'id':'10003', 'name':'Jordan', 'age':21 })

# 3. 写入中文