
# take two int input from user, if one of them(or both) is 10 or sum of both integers is 10 then
# return True else False

def makes10(a,b):
    if (a ==10) or (b == 10) or ((a+b) == 10):
        return True

    else:
        return False

a = int(input("Enter First Number:-"))
b = int(input("Enter Second Number:-"))
rv=makes10(a,b)      #creating object and give reference to "rv"
print(rv)       #printing the return value from function


