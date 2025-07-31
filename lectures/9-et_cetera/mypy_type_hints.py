def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number of meows: "))
meows: str = meow(number)
print(meows, end="")