# N, K : 5 2
# 공유 숫자 카드 : -1 2 3 4 5
# 팀 숫자 카드 : -1 0 2 3 4
# 우리팀이 얻을 수 있는 최대 점수 출력

n, k = list(map(int, input().split()))
common = list(map(int, input().split()))
team = list(map(int, input().split()))
answer = -100000001
max_team = team[0]

for item in range(k+1):
    for x in common:
        for y in team:
            if x*y > answer:
                answer = x*y
                max_team = y

    if item != k:
        team.remove(max_team)
        answer = -100000001


print(answer)


# print(n)
# print(k)
# print(common, team)
