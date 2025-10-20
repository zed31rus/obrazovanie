text = input("Введите строку со скобками: ")
start = text.find('(')
end = text.find(')')
if start != -1 and end != -1 and end > start:
    print("Символы внутри скобок:", text[start+1:end])
else:
    print("Скобки не найдены или некорректный порядок.")