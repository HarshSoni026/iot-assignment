def max_of_three(num1,num2,num3):
    if num1 >= num2:
        if num1>num3:
            print(f"{num1} is greatest")
        else:
            print(f"{num3} is greatest")
    else:    
        if num2 > num3:
            print(f"{num2} is greatest")
        else:
            print(f"{num3} is greatest")

num1 = int(input("num1 is : "))
num2 = int(input("num2 is : "))
num3 = int(input("num3 is : "))

max_of_three(num1, num2, num3)