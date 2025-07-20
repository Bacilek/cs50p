import re

name = input("Name: ").strip()

# walrus operator ':=' -> asssign & at the same time boolean question
if matches := re.search(r"^(.+), ?(.+)$", name): # 1+ x anything + 1x ',' + 0-1x ' ' + 1+ x anything 
    last, first = matches.groups() # last, first = matches.group(1), matches.group(2)
    name = f"{first} {last}"

print(f"hello, {name}")
