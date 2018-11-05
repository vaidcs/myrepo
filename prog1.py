
#program for compairing two numbers and printing bigger number using conditional control statement

x = int(input("Enter 1st Number:-"))
y = int(input("Enter 2st Number:-"))

if x>y:
    print(x,"is bigger than",y)

elif x<y:
    print(y,"is bigger than",x)

else:
    print(x,"and",y,"are same")