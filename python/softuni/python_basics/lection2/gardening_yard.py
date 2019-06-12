# Program that calculates the expenses for gardening of a yard

square_meters = float(input())
#(1-0.18) * total amount
result = square_meters * 7.61
discount = result * 0.18
# Total result of the job
result = result - discount

print(f"The final price is: {result:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")

