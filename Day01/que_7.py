def factorial(num):
    fact = 1
    while(num <= 10):
        fact = num * fact
        print(f"factorial of {num} = {fact}")
        num += 1
        
print(f"factorial of {0} = {1}")
factorial(1)

