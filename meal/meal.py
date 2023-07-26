s = '7:30'
s = s.split(':')
print(s)

a = int(s[0])
b = int(s[1])

if b <= 1 and b >= 30:
    b = b
else:
    b = b + 0.5

print(b)

