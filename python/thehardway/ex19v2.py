# Define the function cheese and crackers and set 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# Print first argument (cheese count)
    print(f"You have {cheese_count} cheeses!")
# Print seocnd argument (boxes of crackers)
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n ")
# Assign numbers to the function directly
print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)
# Sets variables seperately for the function
print("OR, we can use variables from our script:")
amount_of_cheese = 20
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# Uses math to set the numbers for arg1 and arg2
print("We can even use math:")
cheese_and_crackers(10 + 50, 5 * 6)
# Combines the variables and math 
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 200)