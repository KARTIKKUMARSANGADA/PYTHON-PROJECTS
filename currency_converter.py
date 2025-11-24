
print("🌍 WELCOME TO CURRENCY CONVERTER APP")
print("======================================")


rates = {
    "USD": 1,           
    "INR": 83.12,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 151.35
}

def convert(amount, from_curr, to_curr):
    usd_amount = amount / rates[from_curr]    
    final_amount = usd_amount * rates[to_curr]  
    return final_amount

currencies = list(rates.keys())

while True:
    print("\nAvailable Currencies:")
    for i, curr in enumerate(currencies, start=1):
        print(f"{i}. {curr}")

    try:
        choice1 = int(input("\nSelect currency to convert FROM (1-5): "))
        choice2 = int(input("Select currency to convert TO (1-5): "))
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        continue

    if choice1 < 1 or choice1 > 5 or choice2 < 1 or choice2 > 5:
        print(" Invalid choice. Try again.")
        continue

    from_curr = currencies[choice1 - 1]
    to_curr = currencies[choice2 - 1]

    result = convert(amount, from_curr, to_curr)

    print(f"\n {amount} {from_curr} = {round(result, 2)} {to_curr}")

    again = input("\nDo you want to convert again? (y/n): ").lower()
    if again != 'y':
        print("Thank you for using Currency Converter! ")
        break
