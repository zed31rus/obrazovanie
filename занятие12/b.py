def max():
    x = int(input())
    if x == 0:
        return 0
    
    m = max()
    
    return x if x > m else m

print(max())
