def duplicatChr(str):
    str.lower()
    str = str.replace(" ", "")
    # print(str)
    for chr in range (1,len(str)) :
        # print(str[:chr])
        # print(str[chr])
        for letter in str[:chr]:
            if str[chr] == letter:
                print('the repeated chr is : ',str[chr])
                return False
    return True

str = 'The quick brown fox jumps over the lazy dog'
print(duplicatChr(str))