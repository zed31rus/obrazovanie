def count_replace_dot():
    text = input("Введите строку: ")
    count = text.count('.')
    new_text = text.replace('.', '')
    print("Изменённая строка:", new_text)
    print("Количество удалённых символов:", count)

count_replace_dot()