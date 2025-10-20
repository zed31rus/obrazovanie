text = input("Введите текст: ")
word = input("Введите слово для поиска: ")
count = text.lower().split().count(word.lower())
print("Количество вхождений:", count)