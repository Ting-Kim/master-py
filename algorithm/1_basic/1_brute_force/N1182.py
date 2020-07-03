def part_list(sum, index):
    global answer
    if index == a:
        if sum == b:
            answer += 1
        return
    part_list(sum+arr[index], index+1)
    part_list(sum, index+1)

a, b = map(int, input().split())
answer = 0
arr = list(map(int, input().split()))

part_list(0, 0)

if b == 0:
    answer -= 1
print(answer)
