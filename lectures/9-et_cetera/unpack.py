def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# method
print(f"{total(100, 50, 25)} Knuts")

# list
coins = [100, 50, 25]

# list verbose
print(f"{total(coins[0], coins[1], coins[2])} Knuts")

# list unpacking: star unpacks indi idually
print(f"{total(*coins)} Knuts")

# dictionary
coinz = {"galleons": 100, "sickles": 50, "knuts": 25}

# dictionary verbose
print(f"{total(coinz['galleons'], coinz['sickles'], coinz['knuts'])} Knuts")

# dictionary unpacking: double star unpacks individually
print(f"{total(**coinz)} Knuts")