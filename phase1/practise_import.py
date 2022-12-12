import random
import time

n = random.randint(1, 5)

if n == 1:
    print(f"The random number is {n}")
else:
    if n == 2:
        print(f"The random number is {n}")
    else:
        print("The random number is huge!!")

seconds = int(time.time())

if seconds % 3 == 0:
    if seconds % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if seconds % 5 == 0:
        print("Buzz")
    else:
        print(f"{seconds} seconds")

