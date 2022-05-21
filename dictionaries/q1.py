groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
}

# quantity = {
#     "Baby Spinach": 2,
#     "Hot Chocolate": 1,
#     "Crackers": 4,
#     "Bacon": 0,
#     "Carrots": 8,
#     "Oranges": 5
# }

for items, prices in groceries.items():
    #print(f"items: {items}")
    #print(quantity[items])
    total = prices * quantity[items]
    total = "{:.2f}".format(total)
    #print(total)
    print(f"{quantity[items]} {items} @ ${prices} = ${total}")
    

   