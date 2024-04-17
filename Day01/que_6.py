def factorial(num):
    fact = 1
    while(num > 0):
        fact = num * fact
        num-=1
    print(f"factorial = {fact}")
factorial(3)
