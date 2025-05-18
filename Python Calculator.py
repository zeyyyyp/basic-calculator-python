# CALCULATOR!

# This is a simple calculator program that adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
        return x / y

print("Feel free to use this calculator!")
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:
         try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
         except ValueError:
                print("Invalid input. Please enter a number.")
                continue
         if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
                continue
         elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
                continue
         elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
                continue
         elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
                continue
         next_calculation = input("Do you want to perform another calculation? (yes/no): ")
         if next_calculation.lower() != 'no':
                break
         else:
                print("Invalid Input")