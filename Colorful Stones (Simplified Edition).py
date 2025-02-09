s = input()  
t = input()  
pos = 1  
 
for c in t:  
    if s[pos - 1] == c:  
        pos += 1  
 
print(pos)
