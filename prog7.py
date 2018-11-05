
# Write a program input Employee name, salary,
# Designation(m/a/c) .
# If designation is manager then bonus is 20% on his salary
# If designation is analyst then bonus is 10% on his salary
# If designation is clerk then bonus is 5% on his salary.
# Calculate Total salary.


print("WELCOME")

while True:
    name = input("Enter Your Name:-")
    name = name.capitalize()
    sal = float(input("Enter Your Salary:-"))
    deg = input("Enter Your Designation"
                "\npress m/M for Manager"
                "\npress a/A for analyst"
                "\npress c/C for clerk")


    if (deg == "m") or (deg == "M"):
        bonus = 0.2*sal
        sal += bonus
        print("Congratulation", name, "You got Bonus of", bonus, "Rupees\nYour Total Salary is", sal,
              "\nThanks, Enjoy Your Bonus")

    elif (deg == "a") or (deg == "A"):
        bonus = 0.1*sal
        sal += bonus
        print("Congratulation", name, "You got Bonus of", bonus, "Rupees\nYour Total Salary is", sal,
              "\nThanks, Enjoy Your Bonus")

    elif (deg == "c") or (deg == "C"):
        bonus = 0.05 * sal
        sal += bonus
        print("Congratulation", name, "You got Bonus of", bonus, "Rupees\nYour Total Salary is", sal,
              "\nThanks, Enjoy Your Bonus")

    else:
        print("You Entered Wrong Designation...")

    con = input("\nPress Y/y to fill details again...")
    if (con == "Y") or (con == "y"):
        continue
    else:
        break

print("Thanksssss")