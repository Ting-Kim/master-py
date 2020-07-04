# 2차원 배열에서의 극대값 찾기.

#  i ,j = 탐색을 시작할 세로, 가로 인덱스값
def searchMax2D(i, j, array):

    rowMax = max(array[i])
    x = array[i].index(rowMax)

    # 중앙에서부터 시작해서 행이 모서리에 위치하였을 때는 반환.
    if i <= 0 or i >= len(array):
        return array[i][j]

    if array[i][x] < array[i-1][x]:
        searchMax2D(i-1, x, array)
        return
    elif array[i][x] < array[i+1][x]:
        searchMax2D(i+1, x, array)
        return
    else:
        return rowMax


array = [[63, 57, 50, 37, 44], [6, 89, 74, 24, 50],
         [30, 29, 10, 87, 89], [75, 8, 70, 56, 79], [99, 55, 54, 98, 4], [33, 28, 6, 89, 74]]

print(searchMax2D((len(array)-1)//2, (len(array[0])-1)//2, array)
      )
