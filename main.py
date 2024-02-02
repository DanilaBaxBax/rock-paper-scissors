import random
import tkinter as tk
from tkinter import messagebox

# Инициализация счетчиков побед и поражений
wins = 0
losses = 0
draws = 0

def play_game(user_choice):
    global wins, losses, draws

    # Генерация выбора компьютера
    choices = ['r', 's', 'p']
    computer_choice = random.choice(choices)
    
    # Проверка результатов
    if user_choice == computer_choice:
        messagebox.showinfo("Результат", "Ничья!")
        draws += 1
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r'):
        messagebox.showinfo("Результат", "Вы победили!")
        wins += 1
    else:
        messagebox.showinfo("Результат", "Вы проиграли :(")
        losses += 1
    
    # Обновление счетчиков на экране
    wins_label.configure(text=f"Победы: {wins}")
    losses_label.configure(text=f"Поражения: {losses}")
    draws_label.configure(text=f"Ничьи: {draws}")

# Создание графического интерфейса
window = tk.Tk()
window.title("Камень, ножницы, бумага")

label = tk.Label(window, text="Выберите: камень, ножницы или бумага")
label.pack()

button_rock = tk.Button(window, text="Камень", command=lambda: play_game('r'))
button_rock.pack()

button_scissors = tk.Button(window, text="Ножницы", command=lambda: play_game('s'))
button_scissors.pack()

button_paper = tk.Button(window, text="Бумага", command=lambda: play_game('p'))
button_paper.pack()

wins_label = tk.Label(window, text=f"Победы: {wins}")
wins_label.pack()

losses_label = tk.Label(window, text=f"Поражения: {losses}")
losses_label.pack()

draws_label = tk.Label(window, text=f"Ничьи: {draws}")
draws_label.pack()

window.mainloop()
