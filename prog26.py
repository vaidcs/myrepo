# Input any 10 numbers find out no of positive numbers and
# no of negative numbers

ls = [0,0,0,0,0,0,0,0,0,0]

for x in range(10):
    no = int(input("Enter number:-"))
    ls[x] = no

for x in range(10):
    if ls[x]>0:
        print(ls[x],"is positive")
    elif ls[x]<0:
        print(ls[x],"is negative")
    else:
        print("0 is neutral")