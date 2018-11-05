# Input any 10 numbers find the first biggest and second
# biggest number


ls = [0,0,0,0,0,0,0,0,0,0]
fstBig = 0
sndBig = 0

for x in range(10):
    no = int(input("Enter number:-"))
    ls[x] = no

for x in range(10):
    for y in range(10):
        if ls[x]>=ls[y]:
            fstBig = ls[x]
        else:
            fstBig = ls[y]

for x in range(10):
    if ls[x] < fstBig:
        sndBig = ls[x]

print("Biggest no is",fstBig)
print("Second Biggest no is",sndBig)