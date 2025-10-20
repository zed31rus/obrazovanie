text = input("Введите строку: ")
if text.endswith('.'):
    text = text[:-1]
    words = text.split()
    print("Количество слов:", len(words))