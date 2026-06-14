SELECT 書號, 書名
FROM [圖書資料$] 
WHERE 定價 >= 500 AND 書名 LIKE '%程式%';
