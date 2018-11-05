
# Given 2 int values, return True if one is negative and one is
# positive. Except if the parameter "negative" is True, then return
# True only if both are negative
# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True


def pos_neg(a,b,negative):
    if negative == 1:
        # "Negative" is true
        if a<0 and b<0:
            return True
        else:
            return False

    elif negative == 0:
        #"Negative" is false
        if (a<0 and b>0) or (a>0 and b<0):
            return True
        else:
            return False

    else:
        print("Wrong Input")

a = int(input("Enter First Number:-"))
b = int(input("Enter Second Number:-"))
negative = int(input("Enter 'negative' parameter value(1 for True or 0 for False)"))

rv = pos_neg(a,b,negative)
print(rv)