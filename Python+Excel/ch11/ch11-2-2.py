import requests 
 
url = "http://httpbin.org/get?a=15&b=22"
r = requests.get(url)
if r.status_code == 200:
    print(r.text)
else:
    print("錯誤! HTTP請求失敗...")

