
# Input any 4 digit number and reverse it

no = int(input("Enter a Four digit number"))
ls = [0,0,0,0]

for x in range(4):
    ls[x] = no%10
    no = int(no/10)

ls[0] = 1000*ls[0]
ls[1] = 100*ls[1]
ls[2] = 10*ls[2]

reverse = 0
for x in range(4):
    reverse +=ls[x]

print("Reversed No Is",reverse)


# alternate prog

#no = int(input("Enter a Four digit number"))

#a = no%10
#no = int(no/10)
#b = no%10
#no = int(no/10)
#c = no%10
#no = int(no/10)

#a = 1000*a
#b = 100*b
#c = 10*c
#no = 1*no

#print("reverse is",a+b+c+no )