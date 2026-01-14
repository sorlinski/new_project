# 1. Input Variable 
num = int(input("Enter a non-negative integer: "))

# Variable
factorial = 1

# Check
if num < 0:
    print("Can't use Negative Numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    # 2. Start 
    for i in range(1, num + 1):
        factorial = factorial * i
        
    # 3. Print the factorial
    print(f"The factorial of {num} is {factorial}")