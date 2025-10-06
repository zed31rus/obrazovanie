current_count = 1
max_count = 1
prev = None

while True:
    num = int(input())
    if num == 0:
        break
    
    if prev is not None:
        if num == prev:
            current_count += 1
        else:
            current_count = 1
    
    if current_count > max_count:
        max_count = current_count
    
    prev = num

print(max_count)