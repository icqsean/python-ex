def convert_ntd_to_usd(ntd_amount, exchange_rate=29.5):
    """
    將新台幣金額轉換為美金金額的函數。

    Parameters:
    - ntd_amount (float): 輸入的新台幣金額
    - exchange_rate (float, optional): 匯率，預設值為 29.5

    Returns:
    - float: 轉換後的美金金額
    """
    usd_amount = ntd_amount / exchange_rate
    return usd_amount

# 使用者輸入新台幣金額
user_input = float(input("請輸入新台幣金額："))

# 呼叫函數轉換匯率
result_usd = convert_ntd_to_usd(user_input)

# 顯示結果
print("新台幣", user_input, "元等於美金", result_usd, "美元")
