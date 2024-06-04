#binarysearch


arr=[int(x) for x in input("Enter the sorted list of numbers separated by spaces: ").split()]
target = int(input("Enter the target to search:"))

start, end = 0, len(arr)-1
found = False
while start <= end:
    mid = (start+end) //2
    if arr[mid] == target:
        print(f"Target {target} found at index {mid}.")
        found = True
        break
    elif arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
    
if not found:
    print(f"Target {target} not found in the array.")

#time complexity = O(logN)