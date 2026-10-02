import requests

url = "https://postman-echo.com/get"
resp = requests.get(url)
print("状态码：", resp.status_code)
print("返回数据：", resp.json())