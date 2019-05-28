voucher_price = int(input())

purchased_tickets = 0
purchased_products = 0
movie_price = 0
product_price = 0

while voucher_price >= 0 and product_price == 0 and movie_price == 0:
    product = input()

    if product == "End":
        break

    if len(product) > 8:
        for letter in range(len(product)):
            movie_price += (ord(product[letter]))
            if letter == 1:
                break
    elif len(product) <= 8:
        for letter in range(len(product)):
            product_price += (ord(product[letter]))
            break

    if movie_price != 0 and movie_price <= voucher_price:
        voucher_price -= movie_price
        purchased_tickets +=1
        movie_price = 0
    elif product_price != 0 and product_price <= voucher_price:
        voucher_price -= product_price
        purchased_products += 1
        product_price = 0

print(f"{purchased_tickets}")
print(f"{purchased_products}")