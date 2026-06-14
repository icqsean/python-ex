from pathlib import Path

path = Path("temp", "test.txt")
print("檔名:", path.name)
print("副檔名:", path.suffix)
