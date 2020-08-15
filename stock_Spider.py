#-*-  coding = utf-8 -*-  
#@Time : 2020/8/14 15:13
#@Author : 贾先圆
#@File: stock_Spider.py
#@Software: PyCharm

'''
    自动生成请求体
    https://curl.trillworks.com/
'''
import requests

cookies = {
    'st_si': '15183055838180',
    'st_asi': 'delete',
    'waptgshowtime': '2020814',
    'qgqp_b_id': 'f3dc5ef48002e53cb2836e6c8e054820',
    'dRecords': '^%^u4E2A^%^u80A1^%^u8D44^%^u91D1^%^u6D41^%^7Chttp^%^3A//data.eastmoney.com/zjlx/detail.html',
    'cowCookie': 'true',
    'intellpositionL': '1079.19px',
    'HAList': 'a-sz-300059-^%^u4E1C^%^u65B9^%^u8D22^%^u5BCC',
    'em_hq_fls': 'js',
    'intellpositionT': '1055px',
    'st_pvi': '40967750946909',
    'st_sp': '2020-08-14^%^2014^%^3A39^%^3A44',
    'st_inirUrl': 'https^%^3A^%^2F^%^2Fwww.eastmoney.com^%^2F',
    'st_sn': '45',
    'st_psi': '20200814160624456-113300300813-7394911709',
}

headers = {
    'Referer': 'http://data.eastmoney.com/zjlx/detail.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
}

params = (
    ('pn', '1^'),
    ('pz', '50^'),
    ('po', '0^'),
    ('np', '1^'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5^'),
    ('fltt', '2^'),
    ('invt', '2^'),
    ('fid0', 'f4001^'),
    ('fid', 'f62^'),
    ('fs', 'm:0 t:6 f:^!2,m:0 t:13 f:^!2,m:0 t:80 f:^!2,m:1 t:2 f:^!2,m:1 t:23 f:^!2,m:0 t:7 f:^!2,m:1 t:3 f:^!2^'),
    ('stat', '1^'),
    ('fields', 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^'),
    ('rt', '53246312^'),
    # ('cb', 'jQuery183028658536377852073_1597389341243^'),
    ('_', '1597389360898'),
)

url = 'http://push2.eastmoney.com/api/qt/clist/get?pn='


response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies, verify=False)





# response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, verify=False)
# print(response.content)
data = response.text    #<class 'str'>  这里结果是在花括号里，但是这里的类型不是字典类型，是字符串
#
# print(data)
# print(type(data))

# 2. 数据清洗

import json

json_data = json.loads(data)
# print(json_data)    #
# print(type(json_data))  #<class 'dict'>
datas = json_data.get("data").get("diff")
# print(len(data))
# # print(data)
# print(type(data))

companies = []
prices = []
for data in datas:
    # print(data)
    # print(len(data))
#     # print(type(data))
    company = data.get("f14")
    print(company)
    share_1 = data.get('f184')
    print(share_1)
#     share_5 = data.get('f69')
#     share_10 = data.get('f75')
#
# #     当天股价
    price = data.get('f2')
    print(price)
#
    # if share_1 >=10 and share_5>=5 and share_10>=5:
    if share_1 >=-10:
        companies.append(company)
        prices.append(price)
#
#
print(companies)
print(prices)
