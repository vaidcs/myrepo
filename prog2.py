
#program for compairing three numbers and printing biggest number using conditional control statement

x = int(input("Enter 1st Number:-"))
y = int(input("Enter 2nd Number:-"))
z = int(input("Enter 3rd Number:-"))

if (x>y and x>z) :
    print(x,"is biggest")

elif y>x and y>z:
    print(y,"is biggest")

elif z>x and z>y:
    print(z,"is biggest")

elif x==y and x>z:
    print(x,y,"are same and bigger than",z)

elif x==z and x>y:
    print(x,z,"are same and bigger than",y)

elif y==z and y>x:
    print(y,z,"are same and bigger than",x)

else:
    print(x,y,z,"are same")