
# billing program
# show bill according to slab type

print("WELCOME")
name = input("Enter Your Name:-")
name = name.capitalize()
print("Choose Your Slab Type:-\n"
      "1. Industry\n"
      "2. Commercial\n"
      "3. Residence\n")

choice = int(input("Enter Your Choice..."))

if choice == 1:
    unit = int(input("Enter Unit Consumed:-"))
    bill = unit*5.25
    print(name, "Your Bill Is:-", bill, "Rupees only")

elif choice == 2:
    unit = int(input("Enter Unit Consumed:-"))
    bill = unit*4.00
    print(name, "Your Bill Is:-", bill, "Rupees only")

elif choice == 3:
    unit = int(input("Enter Unit Consumed:-"))
    bill = unit*3.08
    print(name, "Your Bill Is:-", bill, "Rupees only")

else:
    print("You Choose Incorrect Option")

print("Thanks")