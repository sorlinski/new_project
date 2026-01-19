import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    nums = [random.randint(1, 100) for _ in range(10)]
    print(f"Original List: {nums}")
    
    sorted_nums = insertion_sort(nums)
    
    print(f"Sorted List:   {sorted_nums}")

if __name__ == "__main__":
    main()