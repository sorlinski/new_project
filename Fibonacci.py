#Variables

n1 = 0
n2 = 1

# 1. Inputs
count = int(input("How many Fibonacci numbers do you want? "))

# 3.Loop
for i in range(count):
    # 4. Print the number of every loop
    print(n1)
    
    # Calculate the next values
    next_num = n1 + n2
    n1 = n2
    n2 = next_num