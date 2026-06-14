SELECT 學生.學號, 學生.姓名, 班級.課程編號, 班級.教授編號
FROM [學生$] AS 學生
INNER JOIN [班級$] AS 班級 ON 學生.學號 = 班級.學號;
