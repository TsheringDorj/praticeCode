while True:
    choice = input("Enter 'F' to convert Fahrenheit to Celsius or 'C' to convert Celsius to Fahrenheit or 'Q' to quit the game: ")
    if choice == 'F':
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature in Celsius: {:.2f}".format(celsius))
    elif choice == 'C':
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius * 9/5 + 32
        print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))
        break
    else: choice == 'Q'
    print("Bye.")
    break