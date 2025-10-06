n = int(input())

p = 1
e = 0

while p * 2 <= n:
    p *= 2
    e += 1

print(e, p)