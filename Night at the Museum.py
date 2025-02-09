
s = input()  
pos = 'a'  
print(sum(min(abs(ord(c) - ord(pos)), 26 - abs(ord(c) - ord(pos))) for pos, c in zip('a' + s, s)))
