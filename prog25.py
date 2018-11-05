
# Input any 10 numbers find out no of even numbers and
# no of odd numbers

ls = [0,0,0,0,0,0,0,0,0,0]

for x in range(10):
    no = int(input("Enter number:-"))
    ls[x] = no

for y in range(10):
    if ls[y] > 1:
        for x in range(2,ls[y]):
            if ls[y]%x == 0:
                print(ls[y],"is Not a Prime Number")
                break
        else:
            print(ls[y],"is a prime no")
    else:
        print(ls[y],"is Not A Prime Number")