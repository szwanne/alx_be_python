num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operator = input("Choose the operation (+, -, *, /):")

match operator:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero"
        print(f"The result is {result}")
