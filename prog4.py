
# Given an int n, return the absolute difference between n and
# 21, except return double the absolute difference if n is over 21.
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

def diff21(x):
    if x<=21:
        y = 21 - x
        return y

    else:
        y = 2*(x - 21)
        return y

x = int(input("Enter A No:-"))
rt = diff21(x)
print("Difference is:-",rt)