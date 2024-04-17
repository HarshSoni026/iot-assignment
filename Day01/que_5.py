def average(sub1, sub2, sub3):
    average = (sub1 + sub2 + sub3)/3
    if(average > 90):
        print("Grade A")
    elif(average > 80):
        print("Grade B")
    elif(average > 70):
        print("Grade C")
    elif(average > 60):
        print("Grade D")
    elif(average > 0):
        print("Grade F")

sub1 = int(input("Enter sub1 mark : "))
sub2 = int(input("Enter sub2 mark : "))
sub3 = int(input("Enter sub3 mark : "))

average(sub1, sub2, sub3)



