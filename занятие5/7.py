prev = int(input())
count = 0

if prev != 0:
    while True:
        current = int(input())
        if current == 0:
            break
        if current > prev:
            count += 1
        prev = current

print(count)