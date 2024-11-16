
num1 = int(input("Enter you first number"))
print(f"The first num = {num1}")

num2 = int(input("Enter you second number"))
print(f"The second num = {num2}")



print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice == "1":
    result = num1 + num2
    print(f"The addition is = {result}")
    
elif choice == "2":
    result = num1 - num2
    print(f"The subtraction is = {result}")
    
elif choice == "3":
    result = num1 * num2
    print(f"The multiplication is = {result}")
    
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"The division is = {result}")
    else:
        print("Division by Zero is not allowed")

else :
    print("Somthing is Wrong!!")
    

    

