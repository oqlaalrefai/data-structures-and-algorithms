def reverseArray(arr):
    '''this function take array as argument and return same array but with reversed element '''
    new_lst = arr[::-1]
    return new_lst

if __name__=="__main__":
    print(f'the reversed array is :  {reverseArray([1,2,3,4,5])}')