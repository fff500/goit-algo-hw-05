def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    counter = 0
    closest = arr[0]
 
    while low <= high:
        mid = (high + low) // 2

        if closest - arr[mid] < closest - x:
            closest = arr[mid]
 
        if arr[mid] < x:
            low = mid + 1
            counter += 1
 
        elif arr[mid] > x:
            high = mid - 1
            counter += 1
 
        else:
            counter += 1
            
    return (counter, arr[mid] if arr[mid] == x else closest)

arr = [2.2, 3.2, 4.2, 10.2, 14.2, 16.2, 17.3, 25.2, 29.4, 31.2]
x = 14.1
result = binary_search(arr, x)
print(result)
