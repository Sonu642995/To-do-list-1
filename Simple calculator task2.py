def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Error! Division by zero."
    return a / b

while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "5":
        print("👋 Exiting Calculator. Thank you!")
        break
    
    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == "1":
            print(f"✅ Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"✅ Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"✅ Result: {num1} × {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"✅ Result: {num1} ÷ {num2} = {divide(num1, num2)}")
    else:
        print("❌ Invalid choice. Please try again.")