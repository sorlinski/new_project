def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    
    return sum(numbers) / len(numbers)

my_numbers = [22, 63, 34, 33, 1]
print(f"The average is: {calculate_average(my_numbers)}")