prices = {}
prices.update({"banana": 4, "apple": 2, "orange": 1.5, "pear": 3})

stock = {}
stock.update({"banana": 6, "apple": 0, "orange": 32, "pear": 15})

for k in prices:
    print(k)
    print("price:", prices[k])
    print("stock:", stock[k])
    print()

total = 0
for k in prices:
    total += prices[k]*stock[k]

print("Total money you will get:", total)
