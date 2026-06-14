from pathlib import Path

path = Path("examples", "Excel1", "營業額1.xlsx")
print(path)

path2 = Path("examples") / Path("Excel1") / Path("營業額1.xlsx")
print(path2)

print(Path("/temp") == Path("/temp"))
print(Path("/temp/a") == Path("/temp/b"))

