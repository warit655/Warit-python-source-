# Complete this ATM simulation
balance = 1000000000
pin = "080632"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:

        if choice == "4":
            print("thx to use ATMM:D")
            break

        if choice == "1":
            print("Now You have ", balance)
            
        if choice =="2":
            bike= float (input("Withdraw amount:"))
            balance = balance - bike
            print("now you have", balance)

        if choice =="3":
            deposit = float (input("Deposit amount:"))
            balance = balance + deposit
            print("now you have", balance)
else:
    print("Invalid PIN plesa try agine")
