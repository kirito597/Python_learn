#包管理器
#requests用于发送网络请求的库
import requests

#模拟浏览器
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'}

#发送一个get请求
resp = requests.get('http://www.baidu.com', headers=headers)

#设置字符编码
resp.encoding = 'utf-8'

#状态码
print(resp.status_code)
if resp.status_code == 200:
    #拿到请求结果
    print(resp.text)
