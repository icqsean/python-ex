import pandas as pd
from pandasql import sqldf

titanic = pd.read_excel("鐵達尼號.xlsx")
titanic2 = titanic.copy()
result = titanic["Age"].isnull().sum()
print("遺漏值數=", result)
print("---------------")
age = round(titanic["Age"].mean())
titanic["Age"] = titanic["Age"].fillna(age)
print(titanic[["Name","Age"]].head(20))
print("---------------")
result = sqldf("""SELECT COUNT(*) AS 遺漏值數 FROM titanic2 
                  WHERE Age IS NULL;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT Round(AVG(Age)) AS 平均值 FROM titanic2 
                  WHERE Age <> "None";
               """)
print(result)


