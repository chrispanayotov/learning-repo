# Stock a supermarket before Exam Sunday. 
# Example - Input: stock Boca_Cola 20, stock Kay's 5, shopping time,
# buy Boca_Cola 5, buy Kay's 5, exam time; Output: Boca_Cola -> 15
data = input().split(' ')
shop_stock = {}

# Stocking the shop before Exam Sunday
while data[0] != 'shopping':
    data[2] = int(data[2])
    # If data[0] is stock then add the products in shop
    if data[0] == 'stock':
        # If product is already in the shop, update the quantity, 
        # else make a new entry
        if data[1] in shop_stock.keys(): 
            shop_stock[data[1]] += data[2]
        else:
            shop_stock[data[1]] = int(data[2])

    data = input().split(' ')

# Exam Sunday has come
data = input().split(' ')

while data[0] != 'exam':
    data[2] = int(data[2])    

    if data[1] in shop_stock:
        # If a product's quantity is less or equal to 0 print out of stock
        if shop_stock[data[1]] <= 0:
            print(f"{data[1]} out of stock")
        # If a student wants to purchase items, but there isn't enough stocked, 
        # sell whatever's left and set the quantity to 0
        elif shop_stock[data[1]] < data[2]:
            shop_stock[data[1]] = 0
        # In any other case make a normal sell
        else:
            shop_stock[data[1]] -= data[2]
    else:
        print(f"{data[1]} doesn't exist")

    data = input().split(' ')

for k, v in shop_stock.items():
    if v <= 0:
        pass
    else:
        print(f"{k} -> {v}")
