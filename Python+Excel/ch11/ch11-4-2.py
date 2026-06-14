import requests
import shutil

fname = "2330TW.csv"
url = "https://query1.finance.yahoo.com/v7/finance/download/2330.TW?period1=1634624307&period2=1666160307&interval=1d&events=history&includeAdjustedClose=true"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
r = requests.get(url, stream=True, headers=headers)

if r.status_code == 200:
    r.raw.decode_content = True
    with open(fname, 'wb') as fp:
        shutil.copyfileobj(r.raw, fp)
    print("已經成功下載CSV檔案:", fname)
