# https://open.kattis.com/problems/princesspeach

obstacles, found = (int(num) for num in input().split())

obstaclesFound = set()

for i in range(found):
    obstaclesFound.add(int(input()))

for i in range(obstacles):
    if i not in obstaclesFound:
        print(i)

print(f'Mario got {len(obstaclesFound)} of the dangerous obstacles.')