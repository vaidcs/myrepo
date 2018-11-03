
# if input in is <= 21 print their difference else print double difference(2*difference)

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