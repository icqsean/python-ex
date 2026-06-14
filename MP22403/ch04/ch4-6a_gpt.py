# 定義匯率
exchange_rate = 29.5

# 接收用戶輸入的新台幣金額
ntd_amount = float(input("請輸入新台幣金額："))

# 計算美金金額
usd_amount = ntd_amount / exchange_rate

# 顯示兌換結果
print("新台幣", ntd_amount, "元等於美金", usd_amount, "美元")
