def BinarySearch(arr,searchKey):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < searchKey:
            low = mid + 1
 

        elif arr[mid] > searchKey:
            high = mid - 1
 
        else:
            return mid
    return -1

print(BinarySearch([0,1,2,3,4,5,6],6))