import requests

fname = "stock.html"	
url = "https://www.taifex.com.tw/cht/3/totalTableDate"
post_data = "queryType=1&goDay=&doQuery=1&dateaddcnt=&queryDate=2022%2F10%2F19"
r = requests.post(url, data=post_data)
if r.status_code == 200:
    r.encoding = "utf-8"
    with open(fname, 'w', encoding="utf8") as fp:
        fp.write(r.text)
 

