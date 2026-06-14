import pandas as pd

tables = pd.read_html("https://fchart.github.io/test/sales.html",
                      match="六")
print("表格數:", len(tables))
df = tables[0]
print(df)
