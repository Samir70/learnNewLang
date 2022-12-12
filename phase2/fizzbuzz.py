def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def generate(n):
    out = "1"
    for i in range(2, n+1):
        out += ", "+fizzbuzz(i)
    return out