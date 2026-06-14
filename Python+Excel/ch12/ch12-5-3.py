import pandas as pd
 
tables = pd.read_html("stock.html")
 
for i in range(len(tables)):
    df = tables[i]
    df.to_excel("stock_table"+str(i)+".xlsx",
                       index=False,
                       engine="openpyxl")
