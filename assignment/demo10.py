
# take two int and return True if ane is -ve and one is +ve or vice versa
# if paramete "negative" is True then return True if both are -ve

def pos_neg(a,b,negative):
    if negative == 1:
        print("Negative is true")
        if a<0 and b<0:
            return True
        else:
            return False

    elif negative == 0:
        print("Negative is false")
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