
# Input any 4 digit number and find out the difference of all
# digits

no = int(input("Enter four digit number"))
ls = []
sum = 0
for x in range(4):
    lsno = no%10
    ls.append(lsno)
    no = int(no/10)

for x in range(4):
    for y in range(4):
        print("Difference between",ls[x],"and",ls[y],"is:-",ls[x]-ls[y])
print("Thanks")