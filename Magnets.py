n = int(input())
magnet_types = [input().strip() for _ in range(n)]

groups = 1
for i in range(1, n):
    if magnet_types[i] != magnet_types[i - 1]:
        groups += 1

print(groups)
