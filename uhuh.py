number =[10, 20, 30, 40, 50, 60, 70]
target = 50
low = 0
high = len(number) - 1
while low <= high:
    mid = (low + high) // 2
    if number[mid] == target:
        print("Target found at index:", mid)
        break
    elif number[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Target not found in the list.")