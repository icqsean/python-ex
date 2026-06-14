import pandas as pd
from pandasql import sqldf

products = pd.read_excel("文具商品採購清單.xlsx",
                   sheet_name="全公司")
result = sqldf("""
SELECT 
    部門,
    SUM(CASE WHEN 分類='書寫用品' AND 項目='原子筆(紅)'
        THEN 數量 END) AS 書寫用品_原子筆紅,
    SUM(CASE WHEN 分類='書寫用品' AND 項目='原子筆(藍)'
        THEN 數量 END) AS 書寫用品_原子筆藍,
    SUM(CASE WHEN 分類='書寫用品' AND 項目='原子筆(黑)'
        THEN 數量 END) AS 書寫用品_原子筆黑,
    SUM(CASE WHEN 分類='紙類用品' AND 項目='便利貼'
        THEN 數量 END) AS 紙類用品_便利貼,
    SUM(CASE WHEN 分類='紙類用品' AND 項目='信封'
        THEN 數量 END) AS 紙類用品_信封,
    SUM(CASE WHEN 分類='紙類用品' AND 項目='筆記本'
        THEN 數量 END) AS 紙類用品_筆記本,
    SUM(CASE WHEN 分類='辦公用品' AND 項目='剪刀'
        THEN 數量 END) AS 辦公用品_剪刀,
    SUM(CASE WHEN 分類='辦公用品' AND 項目='美工刀'
        THEN 數量 END) AS 辦公用品_美工刀,
    SUM(CASE WHEN 分類='辦公用品' AND 項目='釘書機'
        THEN 數量 END) AS 釘書機
FROM products
GROUP BY 部門;
""")
print(result)
result.to_excel("文具商品採購清單樞紐分析表6.xlsx")
