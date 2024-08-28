import tkinter as tk

def on_submit():
    user_input1 = entry1.get()
    user_input2 = entry2.get()
    user_input3 = entry3.get()
    print("Введено:", user_input1, user_input2, user_input3)

# Создаем главное окно
root = tk.Tk()
root.title("Авторизация")

# Получаем размеры экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Устанавливаем размеры формы по полученным данным экрана
root.geometry(f"{screen_width}x{screen_height}")

# Создаем метки и поля ввода с выравниванием по сетке (grid)
label1 = tk.Label(root, text="Пользователь:")
label1.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

entry1 = tk.Entry(root, width=30)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Пароль:")
label2.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

entry2 = tk.Entry(root, width=30)
entry2.grid(row=1, column=1, padx=5, pady=5)

label3 = tk.Label(root, text="ИИН:")
label3.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

entry3 = tk.Entry(root, width=30)
entry3.grid(row=2, column=1, padx=5, pady=5)

# Устанавливаем фокус на первое поле ввода при запуске формы
entry1.focus()

# Кнопка для отправки данных с фиксированным размером и выравниванием
submit_button = tk.Button(root, text="Отправить", command=on_submit, width=15, height=1)
submit_button.grid(row=3, column=1, sticky=tk.E, columnspan=2, pady=5)

# Запускаем главное окно
root.mainloop()
