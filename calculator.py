first = int(input("enter your  first number:"))
operator = input('Enter your operator (+,-,*,/,%):')
second = int(input("enter your second number:"))


if (operator == '+'):
    output= first + second
    print(output)

elif (operator == '-'):
    output= first - second
    print(output)

elif (operator == '*'):
    output= first * second
    print(output)

elif (operator == '/'):
    output= first / second
    print(output)

elif (operator == '%'):
    output= first % second
    print(output)

else:
    print("Invalid operator")



