#Varibles
n = int(input("Enter a number greater than 2 (N): "))

# Loop 
for num in range(2, n + 1):
    
    is_prime = True
    
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False 
            
    if is_prime:
        print(num)