# Read a list of integers, remove all negative numbers from it and print the remaining items in reversed order.
# In case of no items left in the list, print “empty”.

# Solution 1 - basic
data = list(map(int, input().split(" ")))

pure_list = []

for i in range(len(data)):
    x = data.pop()
    if x > 0:
        pure_list.append(x)

if pure_list:
    print(*pure_list)
else:
    print("empty")

# Solution 2 - using lambda function
data = list(map(int, input().split(" ")))

pure_list = list(filter(lambda x: x > 0, data))

if pure_list:
    print(*pure_list)
else:
    print("empty")