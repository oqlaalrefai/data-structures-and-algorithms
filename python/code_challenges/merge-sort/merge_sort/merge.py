def Mergesort(arr):
    n = len(arr)
    if n == 0:
        return 'empty array'
    elif n==1:
        return arr
    elif n > 1:
      mid = n//2
      left = arr[:mid]
      right = arr[mid:]
      Mergesort(left)
      Mergesort(right)
      Merge(left, right, arr)
    return arr

    
def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    if i == len(left):
        arr[k] = right[j]
        j += 1
        k += 1
    else:
       while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
if __name__ == "__main__":
    print(Mergesort([8,4,23,42,16,15]))