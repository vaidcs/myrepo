
print("WElCOME")
m = int(input("Enter marks of Maths:-"))
p = int(input("Enter marks of Physics:-"))
c = int(input("Enter marks of Chemistry:-"))
h = int(input("Enter marks of Hindi:-"))
e = int(input("Enter marks of English:-"))

tm = m+p+c+h+e

if tm>360 and tm<=500:
    print("Congratulation, You got First Class")
elif tm>=300 and tm<360:
    print("You got Second Class")
elif tm<300 and tm>200:
    print("You Got Third Class\n"
          "Better Luck Next Time")
elif tm<200:
    print("You are Fail\n"
          "Better Luck Next Time")
else:
    print("incorrect marks input")
print("Thanksss")