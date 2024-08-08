from pathlib import Path

p1 = Path('./files/ghi.txt')
p2 = Path('./files')

if not p1.exists():
    with open(p1,'w') as file:
        file.write("HELLO WORLD")

print(p1.name)
print(p1.suffix)
print(p1.stem)

#multiple files
for item in p2.iterdir():
    print(item.name)