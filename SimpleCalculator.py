while True:
    print("Welcome to the calculator!!!")
    print("Options:")
    print("Enter 'add' to add two numbers.")
    print("Enter 'subtract' to subtract two numbers.")
    print("Enter 'multiply' to multiply two numbers.")
    print("Enter 'divide' to divide two numbers.")
    print("Enter 'quit' to end the program.")
    user_input = input(": ")
    if user_input == str('quit'):
        break
    elif user_input == str('add'):
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number to add: "))
        result1 = str(num1 + num2)
        print("The answer is " + result1)
        print("Another math question?")
    elif user_input == str('subtract'):
        num3 = float(input("Enter a number: "))
        num4 = float(input("Enter another number to subtract: "))
        result2 = str(num3 - num4)
        print("The answer is " + result2)
        print("Another math question?")
    elif user_input == str('multiply'):
        num5 = float(input("Enter a number: "))
        num6 = float(input("Enter another number to multiply: "))
        result3 = str(num5 * num6)
        print("The answer is " + result3)
        print("Another math question?")
    elif user_input == str('divide'):
        num7 = float(input("Enter a number: "))
        num8 = float(input("Enter another number to divide: "))
        result4 = str(num7 / num8)
        print("The answer is " + result4)
        print("Another math question?")
    else:
        print("Unknow input. Try again!")
