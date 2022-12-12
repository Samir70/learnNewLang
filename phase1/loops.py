num = 2321
sum = 0
while num <= 34325:
    if num % 2 == 0:
        sum += num
    num += 1

print(sum)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(17))


my_list = ["Cat", "Cat", "frog", "Cat", "Dog", "Dog"]
counters = {}

for animal in my_list:
    animal = animal.lower()
    if animal not in counters:
        counters[animal] = 0
    counters[animal] += 1

print(counters)