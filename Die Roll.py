from math import gcd  
 
y, w = map(int, input().split())  
num = 6 - max(y, w) + 1  
den = 6  
g = gcd(num, den)  
 
print(f"{num//g}/{den//g}")
