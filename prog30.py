
# Input any 4 digit number and find out the sum of the

no = int(input("Enter a Four digit number"))
ls = [0,0,0,0]
sum = 0
for x in range(4):
    ls[x] = no%10
    no = int(no/10)

for x in range(4):
    sum +=ls[x]

print("Sum is",sum)