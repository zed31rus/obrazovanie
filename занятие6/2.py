def count_replace_e():
    text = input("Введите строку: ")
    count = text.count(':')
    new_text = text.replace(':', '%')
    print("Изменённая строка:", new_text)
    print("Количество замен:", count)

count_replace_e()