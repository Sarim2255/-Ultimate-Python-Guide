try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    o = input("Enter the desired operation: \nPress + for addition...\nPress - for substraction...\nPress * for multiplication...\nPress / for division...\n")
    match o:
        case "+":
            print(f"The result is {a+b}")
        case "-":
            print(f"The result is {a-b}")
        case "*":
            print(f"The result is {a*b}")
        case "/":
            print(f"The result is {a/b}")
except Exception as e:
    print("Enter the valid number...")