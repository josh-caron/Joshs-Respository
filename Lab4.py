# Lab 4 - Fibonacci / Prime

# Finding the Nth term of a fibonacci sequence
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        num1 = 0
        num2 = 1
        for i in range(3, n+1):
            sum = num1 + num2
            num1 = num2
            num2 = sum
        return num2


# Checking if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Prime factorization
def print_prime_factors(n):

    print(str(n) + ' =', end=' ')

    for i in range (2, n+1):
        while n % i == 0:
            if i < n:
                print(i,'*', end=' ')
                n //= i
            else:
                print(i)
                break







