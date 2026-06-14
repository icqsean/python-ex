# 請輸入您的身高（公分）：
height = float(input("請輸入您的身高（公分）：")) / 100

# 請輸入您的體重（公斤）：
weight = float(input("請輸入您的體重（公斤）："))

# 修正：BMI計算公式應為 weight / (height * height)
bmi = weight / (height * height)

# 顯示BMI值
print("您的BMI值為：", bmi)
