total = 0
count = 0

while True:
    num = int(input())
    if num == 0:
        break
    total += num
    count += 1

if count > 0:
    average = total / count
    print(average)
else:
    print(0)