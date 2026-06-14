from pathlib import Path

path = Path("temp", "test.txt")
with path.open("a") as fp:
    fp.write("陳允傑")
print("檔案內容:", path.read_text())
