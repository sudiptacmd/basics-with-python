from pathlib import Path
import time

p1 = Path('./files')

for items in p1.iterdir():
    newName = "new-" + items.stem + items.suffix
    newPath = items.with_name(newName)
    items.rename(newPath)

time.sleep(2)
for items in p1.iterdir():
    newName = items.stem[4:] + items.suffix
    newPath = items.with_name(newName)
    items.rename(newPath)