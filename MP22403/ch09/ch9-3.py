import pandas as pd

employees = pd.read_excel("研發部2.xlsx", sheet_name="員工")
employee_id = 20120002
new_salary = 100000
new_pension = 600
employees.loc[employees["編號"] == employee_id,["薪水","公積金"]] = \
                              [new_salary, new_pension]
print(employees)
