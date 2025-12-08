import requests
import json
import tkinter as tk
from tkinter import messagebox

def getRepo():
    repositoryAuthor = author.get().strip()
    repositoryName = repo.get().strip()

    if not repositoryAuthor or not repositoryName:
        return messagebox.showerror("Ошибка", "Вы не ввели автора или имя репозитория")

    url = f"https://api.github.com/repos/{repositoryAuthor}/{repositoryName}"
    response = requests.get(url)

    if response.status_code != 200:
        return messagebox.showerror("Ошибка", "Репозиторий не найден")

    data = response.json()

    try:
        filtered = {
            'company': data.get('owner', {}).get('company'),
            'created_at': data.get('created_at'),
            'email': data.get('owner', {}).get('email'),
            'id': data.get('id'),
            'name': data.get('name'),
            'url': data.get('html_url')
        }

        with open('result.json', 'w', encoding='utf-8') as file:
            json.dump(filtered, file, indent=4, ensure_ascii=False)

        messagebox.showinfo('Успешно', 'Данные сохранены в result.json')
    except Exception as e:
        messagebox.showerror("ошибка", str(e))


win = tk.Tk()
win.title("занятие11")

tk.Label(win, text='Введите автора репозитория:').pack()
author = tk.Entry(win, width=50)
author.pack()

tk.Label(win, text='Введите имя репозитория:').pack()
repo = tk.Entry(win, width=50)
repo.pack()

confButton = tk.Button(win, text="Подтвердить", command=getRepo)
confButton.pack()

win.mainloop()
