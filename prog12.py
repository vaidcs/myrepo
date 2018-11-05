
# We have two monkeys, a and b, and the parameters
# a_smile and b_smile indicate if each is smiling. We are in
# trouble if they are both smiling or if neither of them is smiling.
# Return True if we are in trouble
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False


def monkey_trouble(a_smile,b_smile):
    if (a_smile ==1 and b_smile ==1) or (a_smile ==1 and b_smile ==1):
        # we are in trouble
        return True
    elif (a_smile ==1 and b_smile ==2) or (a_smile ==2 and b_smile ==1):
        # we are not in trouble
        return False
    else:
        print("Incorrect Input")

a_smile = int(input("1. Monkey 'a' is smiling"
      "\n2. Monkey 'a' is not smiling"))

b_smile = int(input("\n1. Monkey 'b' is smiling"
      "\n2. Monkey 'b' is not smiling"))

rt = monkey_trouble(a_smile,b_smile)
print(rt)