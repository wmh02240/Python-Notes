#coding = utf-8
'''
Author:wangmh
Email:minhuiwon@163.com
wechat:wmh02240
data:2019/8/19 19:55
desc:
'''
import requests

# headers = {
# 	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
# }
# response = requests.get("https://www.zhihu.com/hello.html", headers = headers)
# print(response.status_code)
# exit() if response.status_code == requests.codes.ok else print("404 not_found!")
# print(response.history)
# print(response.status_code)
# print(type(response))
# print(response.cookies, type(response.cookies))
# print(response, type(response))
# print(response.content) #返回二进制编码内容


response = requests.get("https:/www.baidu.com")
print(response)




		