import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_arr = []
    while left and right:
        
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
            
    return sorted_arr + left + right

def main():
    
    nums = [random.randint(1, 100) for _ in range(10)]
    print(f"Original: {nums}")
        
    sorted_nums = merge_sort(nums)
    
    print(f"Sorted:   {sorted_nums}")

if __name__ == "__main__":
    main()