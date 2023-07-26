s = input('time: ')
s = s.split(':')
print(s)

a = int(s[0])
b = int(s[1])

if b <= 1 and b >= 30:
    b = 0.5
else:
    b = a + 0.5

print(b)

