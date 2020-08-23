import random

num1 = random.randint(0, 500)
n = 1
score = 100

while n:
    print("Enter The Number")
    num2 = int(input())
    score -= 5

    if num2 > num1:
        print("Your Number Is Grater Than The Original Number")
        print("Try Again")

    elif num1 > num2:
        print("Your Number Is Lesser Than The Original Number")
        print("Try Again")

    elif num1 == num2:
        print("You Won The Game")
        n = 0

    if score == 0:
        break
print(f"score = {score}")
