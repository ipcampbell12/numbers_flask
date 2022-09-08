import math

my_num = 25 

def get_digits(number):
    digits = len(str(number))
    return f"{number} has {digits} digits"



def get_square_root(number):
    num = int(number)
    sqrt = math.sqrt(num)
    return f"The square root of {num} is {sqrt}"



def squared(number):
    num = int(number)
    sqrd = num**2
    return f"{num} squared is {sqrd}"




def even_odd(number):
    num = int(number)
    status = ''
    if num % 2 == 0:
        status = 'even'
    if num % 2 != 0:
        status = 'odd'
    return f"{number} is an {status} number"



def prime_composite(number):
    num = int(number)
    flag = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = True
                break
    if flag == True:
        return f"{num} is a composite number"
    else:
        return f"{num} is a prime number"



