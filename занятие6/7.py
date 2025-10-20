text = input("Введите строку: ")
n = len(text)
half = n // 2
first_half = text[:half].replace('п', '*')
new_text = first_half + text[half:]
print("Результат:", new_text)