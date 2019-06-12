# Make a program that calculates the required money 
# to complete a gardening project

yard_area = int(input())
total_price = yard_area * 7.61
discount = 0.18 * total_price
final_price = total_price - discount

print(f"The final price is {final_price:.2f} lv.")
print(f"the discount is {discount:.2f} lv.")
