print("WELCOME TO CURRENCY CONVERTER APP")
print("===================================")

while True:
    print("*****************************")
    print("1. USD")
    print("2. EUR")
    print("3. GBP")
    print("4. JPY")
    print("5. IND")
    choice1 = int(input("Select the currency you want to convert from: "))
    print("You selected option:", choice1)
    print("*****************************")
    print("1. USD")
    print("2. EUR")
    print("3. GBP")
    print("4. JPY")
    print("5. IND")
    choice2 = int(input("Select the currency you want to convert to :"))
    print("You selected option:", choice2)
    print("*****************************")

    amount = int(input(f" Enter amount  you want to convert:"))

    print("===================================")


    if choice1==1 and choice2==1 or choice1==2 and choice2==2 or choice1==3 and choice2==3 or choice1==4 and choice2==4 or choice1==5 and choice2==5:
        print("You selected the same currency for conversion.")
    elif choice1==1 and choice2==2:
        print("You selected to convert from USD to EUR")
        print("Conversion rate is 0.85")
        print("converted currency is:", amount * 0.85)
    elif choice1==1 and choice2==3:
        print("You selected to convert from USD to GBP")
        print("Conversion rate is 0.75")
        print("converted currency is:", amount * 0.75)
    elif choice1==1 and choice2==4:
        print("You selected to convert from USD to JPY")
        print("Conversion rate is 110.0")
        print("converted currency is:", amount * 110.0)
    elif choice1==1 and choice2==5:
        print("You selected to convert from USD to IND")
        print("Conversion rate is 74.0")
        print("converted currency is:", amount * 74.0)
    elif choice1==2 and choice2==1: 
        print("You selected to convert from EUR to USD")
        print("Conversion rate is 1.18")
        print("converted currency is:", amount * 1.18)
    elif choice1==2 and choice2==3:
        print("You selected to convert from EUR to GBP")
        print("Conversion rate is 0.88")
        print("converted currency is:", amount * 0.88)
    elif choice1==2 and choice2==4:
        print("You selected to convert from EUR to JPY")
        print("Conversion rate is 129.53")
        print("converted currency is:", amount * 129.53)

    elif choice1==2 and choice2==5:
        print("You selected to convert from EUR to IND")
        print("Conversion rate is 86.0")
        print("converted currency is:", amount * 86.0)
    elif choice1==3 and choice2==1:
        print("You selected to convert from GBP to USD")
        print("Conversion rate is 1.33")
        print("converted currency is:", amount * 1.33)
    elif choice1==3 and choice2==2:
        print("You selected to convert from GBP to EUR")
        print("Conversion rate is 1.14")
        print("converted currency is:", amount * 1.14)
    elif choice1==3 and choice2==4:
        print("You selected to convert from GBP to JPY")
        print("Conversion rate is 147.0")
        print("converted currency is:", amount * 147.0)
    elif choice1==3 and choice2==5:
        print("You selected to convert from GBP to IND")
        print("Conversion rate is 101.0")
        print("converted currency is:", amount * 101.0)
    elif choice1==4 and choice2==1:
        print("You selected to convert from JPY to USD")
        print("Conversion rate is 0.0091")
        print("converted currency is:", amount * 0.0091)
    elif choice1==4 and choice2==2:
        print("You selected to convert from JPY to EUR")
        print("Conversion rate is 0.0077")
        print("converted currency is:", amount * 0.0077)
    elif choice1==4 and choice2==3:
        print("You selected to convert from JPY to GBP")
        print("Conversion rate is 0.0068")
        print("converted currency is:", amount * 0.0068)
    elif choice1==4 and choice2==5:
        print("You selected to convert from JPY to IND")
        print("Conversion rate is 0.69")
        print("converted currency is:", amount * 0.69)
    elif choice1==5 and choice2==1:
        print("You selected to convert from IND to USD")
        print("Conversion rate is 0.013")
        print("converted currency is:", amount * 0.013)
    elif choice1==5 and choice2==2:
        print("You selected to convert from IND to EUR")
        print("Conversion rate is 0.012")
        print("converted currency is:", amount * 0.012)
    elif choice1==5 and choice2==3:
        print("You selected to convert from IND to GBP")
        print("Conversion rate is 0.0099")
        print("converted currency is:", amount * 0.0099)
    elif choice1==5 and choice2==4:
        print("You selected to convert from IND to JPY")
        print("Conversion rate is 1.45")
        print("converted currency is:", amount * 1.45)
    else:
        print("Invalid choice. Please select a valid option.")

    cont = input("Do you want to perform another conversion? (yes/no): ")

    if cont.lower() != 'yes':
        break



    
        
