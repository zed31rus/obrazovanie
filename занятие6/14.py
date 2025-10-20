text = input("Введите строку: ")
words = text.split()
result = [w for w in words if w.startswith('а') or w.endswith('я')]
print("Подходящие слова:", result)