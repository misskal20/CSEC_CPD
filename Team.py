n = int(input())
count = 0

for i in range(n):
    skills = list(map(int, input().split()))
    if sum(skills) >= 2:
        count += 1

print(count)
