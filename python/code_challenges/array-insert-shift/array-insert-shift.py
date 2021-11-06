def insertShiftArray(arr,val):


    midpoint = len(arr)//2        

    arr = arr[0:midpoint+1] + [val] + arr[midpoint+1:]  

    return arr

print(insertShiftArray([1,4,7,8,9],'oqla'))

