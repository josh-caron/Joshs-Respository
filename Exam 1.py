# Exam 1 Practice

# Random number generator guessing game
def guessing_game(guess):
    if guess == answer:
        print("Congrats! You guessed the correct number!")
    elif guess < answer:
        print("Too low! Guess again!")
    elif guess > answer:
        print("Too high! Guess again!")

answer = 7 #Random number



# Nayarana's Cow Sequence
def nayaranas_cow(index):
    if index == 1:
        print('1')
    elif index == 2:
        print('1')
    elif index == 3:
        print('1')
    else:
        num1 = 1
        num2 = 1
        num3 = 1
        for i in range(4, index+1):
            sum = num1 + num3
            num1 = num2
            num2 = num3
            num3 = sum
        return num3



# Collatz Conjecture (how many steps)
def collatz(n):
    counter = 0
    while n != 1:
        counter += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return counter














