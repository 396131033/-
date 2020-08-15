#-*-  coding = utf-8 -*-  
#@Time : 2020/8/14 16:40
#@Author : 贾先圆
#@File: 10page_stock_Spider.py
#@Software: PyCharm

import requests
import json

headers = {
    'Referer': 'http://data.eastmoney.com/zjlx/detail.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
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
all_data_list = []
for i in range(80,81):   #总共82页，爬取的数据好像默认升序排列的，可以改变页数
    print("........正在抓取第{}页数据........".format(i))
    response = requests.get(url+str(i), headers=headers, params=params, verify=False)
    data = response.content
    # print(data)
    # print(type(data))

    json_data = json.loads(data)
    # print(json_data)
    list_data = json_data.get("data").get("diff")
    # print(len(list_data))
    for item in list_data:

        all_data_list.append(item)

print(len(all_data_list))
print(type(all_data_list))

companies = []
prices = []
for data in all_data_list:
    # print(data)
    # print(len(data))
    #     # print(type(data))

    company = data.get("f14")
    # print(company)
    share_1 = data.get('f184')
    # share_5 = data.get('f165')
    # print("share_5: ",share_5)
    print("share: ", share_1)
    # print(type(share_1))
    # print()
    # #     当天股价
    price = data.get('f2')
    # print(price)
    #
    # if share_1 >=10 and share_5>=5 and share_10>=5:
    if share_1 == '-':
        break
    else:
        if share_1 >= 10:
            print("=====test====")
            companies.append(company)
            prices.append(price)

print("="*20+"抓取完毕","="*20)
print(companies)
print(prices)
print(len(prices))

# 第三步 数据可视化
from pyecharts.charts import Bar
from pyecharts import options as opt
bar = Bar()
bar.add_xaxis(companies)
bar.add_yaxis("股价图",prices)

bar.set_global_opts(
    xaxis_opts=opt.AxisOpts(
        axislabel_opts=opt.LabelOpts(rotate=-45)
            ),
    yaxis_opts=opt.AxisOpts(name="价格：（元/股）")
)

bar.render("股价图2.html")

