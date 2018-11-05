
# WAP to Check the number is prime or not


no = int(input("Enter a number"))
if no >1:
    for x in range(2,no):
        if no%x == 0:
            print("It is Not a Prime Number")
            break
    else:
        print("it is a prime no")
else:
    print("It is Not A Prime Number")