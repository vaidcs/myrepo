
# Input any 4 digit number and find out the sum of middle
# digits(in this prog we can give any lenght of no)


rng = int(input("How many digit no you want to Enter:-"))
no = int(input("Enter number"))
ls = []
sum = 0
for x in range(rng):
    lsno = no%10
    ls.append(lsno)
    no = int(no/10)
print("Sum of First and Last no is:-",ls[1]+ls[2])