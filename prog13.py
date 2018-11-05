
# Given two int values, return their sum. Unless the two
# values are the same, then return double their sum.
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8


def sum_double(x,y):
    if x == y:
        print("2(Sum) is:-", 2*(x+y))
    else:
        print("Sum is:-", x+y)

x = int(input("Enter 1st number:-"))
y = int(input("Enter 2nd number:-"))

sum_double(x,y)