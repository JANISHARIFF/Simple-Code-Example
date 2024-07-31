# write a program to calculate the factorial of number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)   
n = 5 if n is None else n  # Replace with your desired number for testing
print("the factorial of the number " n, "is", factorial(n))




