from random import choice as ch, randint, shuffle

coin = ch(["heads", "tails"])
print(f"Coin flip: {coin}")

print(f"Random 1-10: {randint(1,10)}")

CARDS = ["JACK", "QUEEN", "KING", "ACE"]
for card in CARDS:
    print(card)
