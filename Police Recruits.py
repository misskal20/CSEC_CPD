n = int(input())  
events = list(map(int, input().split()))  
officers = untreated = 0  
 
for e in events:  
    if e == -1:  
        untreated += officers == 0  
        officers = max(0, officers - 1)  
    else:  
        officers += e  
 
print(untreated)
