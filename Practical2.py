# Searching Algorithms in Python

#Linear Search
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search
'''
Time Complexity: O(log n)
Space Complexity: O(1)
'''

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
        
    return -1

def main():
    n = int(input("Enter number of elements: "))
    
    arr = list(map(int, input("Enter elements:\n").split()))
    
    key = int(input("Enter element to search: "))
    
    print("\n Search Algorithms")
    print("1. Linear Search")
    print("2. Binary Search")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        pos = linear_search(arr, key)
        
    elif choice == 2:
        pos = binary_search(arr, key)
        
    else:
        print("Invalid choice")
        return
    
    if pos == -1:
        print("Element not found")
    else:
        print(f"Element found at position {pos+1}")
        
if __name__ == "__main__":
    main()