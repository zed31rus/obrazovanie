def sumfact(n):
    total_sum = 0
    current_fact = 1
    for i in range(1, n+1):
        current_fact *= i
        total_sum += current_fact
    return(total_sum)

a = int(input("введите число для получения суммы факториалов от 1! до факторила вашего числа: "))

print(f"суммой факториалов от 1! до {a}! = {sumfact(a)}")