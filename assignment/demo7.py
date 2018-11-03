
# Atm money withdraw program

print("Welcome To SBI ATM\n")
dlim = 20000
bal = 50000
pin = 1234
x = int(input("Enter Your Pin:-"))
if x == pin:
    print("1. Withdraw Money\n"
      "2. Check Balance\n"
      "3. Check Daily Limit\n")

    x = int(input("Enter Your Choice"))

    if x == 1:
        amt = int(input("Enter Amount To Withdraw:-"))
        if amt%100==0:
            if amt <= bal:
                if amt <= dlim:
                    print("Transection Successful\n"
                          "Collect You Money\n")
                    bal-=amt
                    print("Your Remaining Balance is:-",bal)
                else:
                    print("You Exceed Daily Limit\n"
                          "Daily limit is 20000 rs only")

            else:
                print("Insufficiant Fund")

        else:
            print("You Entered Incorrect Amount")

    elif x == 2:
        print("Your Balance is:-",bal)

    elif x == 3:
        print("Daily Limit is:-",dlim)

    else:
        print("You Choose Incorrect Option")

else:
    print("Incorrect Pin")

print("Thanks For Using ATM")