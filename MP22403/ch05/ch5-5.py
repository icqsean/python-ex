import pandas as pd

tables = pd.read_html("https://fchart.github.io/test/sales.html")
print("表格數:", len(tables))
df = tables[0]
print(df)
print("----------------")
df2 = tables[1]
print(df2)
