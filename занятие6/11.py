text = input("Введите строку: ")

new_text = text.replace('!', '.')

max_seq = 0
current_seq = 0

for ch in text:
    if ch == 'н':
        current_seq += 1
        if current_seq > max_seq:
            max_seq = current_seq
    else:
        current_seq = 0

print("Преобразованная строка:", new_text)
print("Самая длинная последовательность 'н':", max_seq)