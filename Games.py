n = int(input())  
teams = [tuple(map(int, input().split())) for _ in range(n)]  
print(sum(h == a for h, _ in teams for _, a in teams))
