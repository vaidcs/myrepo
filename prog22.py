
# Find the factorial of a given number

no = int(input("Enter a no:-"))
fact = 1

if no != 0:
    for x in range(1,no+1):
        fact *=x
    print(fact)
else:
    print("0")