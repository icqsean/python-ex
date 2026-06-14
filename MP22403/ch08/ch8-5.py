import pandas as pd
from pandasql import sqldf

employees = pd.read_excel("銷售系統.xlsx", sheet_name="員工")
count_salary = employees["薪水"].count()
sum_salary = employees["薪水"].sum()
max_salary = employees["薪水"].max()
min_salary = employees["薪水"].min()
avg_salary = employees["薪水"].mean()
print("計數:", count_salary)
print("總和:", sum_salary)
print("最大:", max_salary)
print("最小:", min_salary)
print("平均:", avg_salary)
print("---------------")
print(employees["薪水"].describe())
print("---------------")
var_salary = employees["薪水"].var()
std_dev_salary = employees["薪水"].std()
print("變異數:", var_salary)
print("標準差:", std_dev_salary)
print("---------------")
result = sqldf("""SELECT COUNT(薪水) AS 計數
                  FROM employees;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT SUM(薪水) AS 總和,
                         MAX(薪水) AS 最大,
                         MIN(薪水) AS 最小,
                         AVG(薪水) AS 平均 
                  FROM employees;
               """)
print(result)
print("---------------")
result = sqldf("""SELECT SUM((薪水-(SELECT AVG(薪水)
                                    FROM employees))*
                             (薪水-(SELECT AVG(薪水)
                               FROM employees)))/
                         (COUNT(薪水)-1) AS 變異數,
                         SQRT(SUM((薪水-(SELECT AVG(薪水)
                                         FROM employees))*
                                  (薪水-(SELECT AVG(薪水)
                                         FROM employees)))/
                        (COUNT(薪水)-1)) AS 標準差
                  FROM employees;
               """)
print(result)
