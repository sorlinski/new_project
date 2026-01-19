import random
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
def main():
    random_list = [random.randint(1, 100) for _ in range(10)]
    print(f"Original Random List: {random_list}")
    sorted_list = bubble_sort(random_list)
    print(f"Sorted List:          {sorted_list}")

if __name__ == "__main__":
    main()