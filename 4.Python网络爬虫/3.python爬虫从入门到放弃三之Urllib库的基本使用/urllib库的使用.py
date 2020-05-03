#coding = utf-8
'''
Author:wangmh
Email:minhuiwon@163.com
wechat:wmh02240
data:2019/8/19 11:50
desc:
'''
#参考地址：https://www.cnblogs.com/zhaof/p/6910871.html

# import urllib
#
# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.read().decode("utf-8"))

import requests

response = requests.get("https://img1.gtimg.com/ninja/2/2019/08/ninja156565667913990.png")
print(response.text)
print(response.headers)
print(response.status_code)
print(response.content)

with open("./1.png","wb") as f:
	f.write(response.content)
	f.close()
