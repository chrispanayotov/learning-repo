# You are given an array (which will have a length of at least 3, but could be 
# very large) containing integers. The array is either entirely comprised of odd 
# integers or entirely comprised of even integers except for a single integer N. 
# Write a method that takes the array as an argument and returns this "outlier" N.


def find_outlier(integers):
    even = [i for i in integers if i % 2 == 0]
    odd = [i for i in integers if not i % 2 == 0]
    if len(even) > len(odd):
        return odd[0]
    else:
        return even[0]

find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) # == 11