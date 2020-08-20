# 导入相应的文件
import requests
import json
import time
# import pymongo

# 连接数据库
# client = pymongo.MongoClient('localhost', 27017)

# 创建数据库和数据集合
# mydb = client['mydb']
# lagou = mydb['lagou']

# 加入请求头
headers = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Referer":"https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                 "(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
}


# 获取cookies值
def get_cookie():
    # 原始网页的URL
    url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    s = requests.Session()
    s.get(url, headers = headers, timeout = 3)  # 请求首页获取cookies
    cookie = s.cookies  # 为此次获取的cookies
    return cookie


# 定义获取页数的函数
def get_page(url, params):
    html = requests.post(url, data = params, headers = headers, cookies = get_cookie(), timeout = 5)

    # 将网页的Html文件加载为json文件
    json_data = json.loads(html.text)
    # 解析json文件，后跟中括号为解析的路径
    total_Count = json_data['content']['positionResult']['totalCount']

    page_number = int(total_Count / 15) if int(total_Count / 15) < 30 else 30

    # 调用get_info函数，传入url和页数
    get_info(url, page_number)


# 定义获取招聘信息函数
def get_info(url, page):
    for pn in range(1, page + 1):
        # post请求参数
        params = {
            "first":"true",
            "pn":str(pn),
            "kd":"python"
        }

        # 获取信息 并捕获异常
        try:
            html = requests.post(url, data = params, headers = headers, cookies = get_cookie(), timeout = 5)
            print(url, html.status_code)
            # 将网页的Html文件加载为json文件
            json_data = json.loads(html.text)
            # 解析json文件，后跟中括号为解析的路径
            results = json_data['content']['positionResult']['result']

            for result in results:
                infos = {

                    # positionName: "python"
                    #
                    # companyFullName: "深圳云安宝科技有限公司"
                    # companySize: "15-50人"
                    # industryField: "信息安全,数据服务"
                    # financeStage: "A轮"
                    #
                    # firstType: "开发|测试|运维类"
                    # secondType: "后端开发"
                    # thirdType: "Python"
                    #
                    # positionLables: ["云计算", "大数据"]
                    #
                    # createTime: "2020-02-02 12:51:01"
                    #
                    # city: "深圳"
                    # district: "南山区"
                    # businessZones: ["科技园"]
                    #
                    # salary: "15k-30k"
                    # workYear: "3-5年"
                    # jobNature: "全职"
                    # education: "本科"
                    #
                    # positionAdvantage: "地铁口近 周末双休"

                    "positionName":result["positionName"],

                    "companyFullName":result["companyFullName"],
                    "companySize":result["companySize"],
                    "industryField":result["industryField"],
                    "financeStage":result["financeStage"],

                    "firstType":result["firstType"],
                    "secondType":result["secondType"],
                    "thirdType":result["thirdType"],

                    "positionLables":result["positionLables"],

                    "createTime":result["createTime"],

                    "city":result["city"],
                    "district":result["district"],
                    "businessZones":result["businessZones"],

                    "salary":result["salary"],
                    "workYear":result["workYear"],
                    "jobNature":result["jobNature"],
                    "education":result["education"],

                    "positionAdvantage":result["positionAdvantage"]
                }
                print(infos)
                # 插入数据库
                # lagou.insert_one(infos)
                # 睡眠2秒
                time.sleep(2)
        except requests.exceptions.ConnectionError:
            print("requests.exceptions.ConnectionError")
            pass


# 主程序入口
if __name__ == '__main__':
    url = "https://www.lagou.com/jobs/positionAjax.json"
    # post请求参数
    params = {
        "first":"true",
        "pn":1,
        "kd":"python"
    }
    get_page(url, params)
