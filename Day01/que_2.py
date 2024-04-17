def face_value(num):
    str1 = " "
    rem = 0

    while(num > 0):
        rem = num % 10
        str1 = f"{rem} {str1}"
        num = num//10

    print(f"face value {str1}")

def place_value(num):
    str2 = ""
    place = 1
    rem = 0
    place_value = 0

    while(num > 0):
        rem = num % 10
        place_value = rem * place
        if(place == 1):
            str2 = str(place_value)
        else:
            str2 = str(place_value) + " + " + str2
        place = place * 10
        num = num // 10
    print(f"palce value {str2}")

def reverse_value(num):
    rem = 0
    reverse = 0

    while(num > 0):
        rem = num % 10
        reverse = (reverse*10) + rem
        num = num//10

    print(f"reverse value {reverse}")


num = int(input("Enter four digit number : "))

face_value(num)
place_value(num)
reverse_value(num)
