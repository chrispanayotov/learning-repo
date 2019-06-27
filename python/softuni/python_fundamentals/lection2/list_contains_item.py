# Read a list of integers on the first line of the console and 
# an integer N from the second line of the console and print whether the item is contained in the list.
#  If it is, print “yes”, otherwise print “no”.
# Example I/O: 

nums = list(map(int, input().split()))
n = int(input())

is_in_list = False

for i in nums:
    if i == n:
        is_in_list = True

if is_in_list:
    print("yes")
else:
    print("no")