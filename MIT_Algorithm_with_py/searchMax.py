def searchMax(start, end, array):
    middle = (start+end)//2
    if middle <= start or middle >= end:
        return array[middle]

    if array[middle-1] > array[middle]:
        return searchMax(start, middle, array)
    elif array[middle] < array[middle+1]:
        return searchMax(middle+1, end, array)
    else:
        return array[middle]


test = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7, 8, 7, 5, 3, 3, 3, 7, 8]
print("극대값을 찾을 배열 : ", test)
print("찾은 극대값 : ", searchMax(0, len(test)-1, test))
