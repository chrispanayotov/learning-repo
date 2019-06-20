n1 = int(input())
n2 = int(input())
operator = input()

result = None
even_odd = None

if n1 == 0:
    print(f"Cannot divide {n2} by zero")
elif n2 == 0:
    print(f"Cannot divide {n1} by zero")

if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2

if operator == "/" and (n1 != 0 and n2 != 0):
    result = n1 / n2
elif operator == "%" and (n1 != 0 and n2 != 0):
    result = n1 % n2

if (operator == "+" or operator == "-" or operator == "*") and (result % 2 == 0):
    even_odd = "even"
elif (operator == "+" or operator == "-" or operator == "*") and (result % 2 != 0):
    even_odd = "odd"

if operator == "+" or operator == "-" or operator == "*":
    print(f"{n1} {operator} {n2} = {result} - {even_odd}")
elif operator == "/" and (n1 != 0 and n2 != 0):
    print(f"{n1} {operator} {n2} = {result:.2f}")
elif operator == "%" and (n1 != 0 and n2 != 0):
    print(f"{n1} {operator} {n2} = {result}")
