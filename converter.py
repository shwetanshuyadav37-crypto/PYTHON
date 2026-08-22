while True:
    print("/nMENU")
    print("1.CM to FT")
    print("2.KM to miles")
    print("3.USD to INR")
    print("4.Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        cm = float(input("Enter cm: "))
        print("Feet =", cm/30.48)
    elif choice == 2:
        km = float(input("Enter km: "))
        print("miles =",km*0.621371)
    elif choice == 3:
        usd = float(input("Enter usd: "))
        print("INR =", usd*91)
    elif choice == 4:
        print("Program ended.")
        break
    else:
        print("Invalid choice")