
# calculate mtotal marks and percentage and show whether it is First second or third class
# Write a program input Total Marks.

# If tm>360 and tm<=500 then print ‘First class’
# If Tm>=300 and tm<360 then print ‘second class’
# If tm<300 then print ‘third class’


print("WElCOME")
m = int(input("Enter marks of Maths:-"))
p = int(input("Enter marks of Physics:-"))
c = int(input("Enter marks of Chemistry:-"))
h = int(input("Enter marks of Hindi:-"))
e = int(input("Enter marks of English:-"))

tm = m+p+c+h+e

if tm>360 and tm<=500:
    print("Congratulation, You scored", tm/5,"% and got First Class")
elif tm>=300 and tm<360:
    print("You scored", tm/5,"% and got Second Class")
elif tm<300 and tm>200:
    print("You scored", tm/5,"% and Got Third Class\n"
          "Better Luck Next Time")
elif tm<200:
    print("You are Fail\n"
          "Better Luck Next Time")
else:
    print("incorrect marks input")
print("Thanksss")