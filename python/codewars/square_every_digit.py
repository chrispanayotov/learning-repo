# In this problem, you have to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    y = ''
    for i in str(num):
        x = int(i)**2
        y += str(x)
    return int(y)

square_digits(9119) # ==  int(811181)