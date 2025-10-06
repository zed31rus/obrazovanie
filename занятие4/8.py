n = int(input("введите число меньше 9 для создания \"лесенки\": "))
print("лесенка из чисел: ")
for i in range(1, n+ 1):
    result = ""
    for l in range(1, i + 1):
        result += str(l)
    print(result)