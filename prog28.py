
# Input any 10 find number of prime numbers


ls = [0,0,0,0,0,0,0,0,0,0]
primeno = 0
for x in range(10):
    no = int(input("Enter number:-"))
    ls[x] = no

for y in range(10):
    if ls[y] > 1:
        for x in range(2,ls[y]):
            if ls[y]%x == 0:
                break
        else:
            primeno +=1
    else:
        continue

print("Total no of Prime numbers out of 10 are",primeno)