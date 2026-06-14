from pathlib import Path

path = Path("temp", "test.txt")
print(path.is_file())
print(path.is_dir())

path2 = Path("examples", "Excel1")
print(path2.is_file())
print(path2.is_dir())