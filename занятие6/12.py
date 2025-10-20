text = input("Введите строку: ")
words = text.split()
count = 0

for word in words:
    if word.endswith('я'):
        print(word)
        count += 1

print("Количество слов, оканчивающихся на 'я':", count)