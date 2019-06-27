# Write a program to read a list of strings, rotate it to the right and print its rotated items.

str_list = input().split(" ")

a = str_list.pop()
str_list.insert(0, a)
print(*str_list)

# Another solution
x = input().split(" ")

p = 1

x[p:] + x[:p]
x[-p:]+x[:-p]