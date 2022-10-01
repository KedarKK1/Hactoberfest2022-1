def decimalToBinaryHexadecimal():
    a = "y"
    while(a == "y" or a == "Y"):
        print("Enter Decimal No : ")
        length = int(input())
        print("1. Decimal to Binary")
        print("2. Decimal to Hexadecimal")
        print("Enter your choice")
        choice = int(input())
        if(choice == 1):
            print(bin(length).replace("0b", ""))
            print("Do you want to continue? (y/n)")
            a = input()
        elif(choice == 2):
            print(hex(length).replace("0x", ""))
            print("Do you want to continue? (y/n)")
            a = input()
        else:
            break

decimalToBinaryHexadecimal()