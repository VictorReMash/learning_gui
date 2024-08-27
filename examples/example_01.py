import tkinter as tk
from tkinter import messagebox

def submit_data():
    # Получаем данные, введенные пользователем
    user_input = entry.get()

    # Проверяем, что поле ввода не пустое
    if user_input.strip() == "":
        messagebox.showwarning("Внимание", "Поле ввода не должно быть пустым!")
    else:
        # Отображаем введенные данные в метке
        result_label.config(text=f"Вы ввели: {user_input}")

# Создаем главное окно
root = tk.Tk()
root.title("Пример ввода данных")

# Создаем метку для инструкций
instruction_label = tk.Label(root, text="Введите что-нибудь:")
instruction_label.pack(pady=10)

# Создаем поле ввода
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Создаем кнопку для отправки данных
submit_button = tk.Button(root, text="Отправить", command=submit_data)
submit_button.pack(pady=10)

# Создаем метку для отображения результата
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Запускаем главное окно
root.mainloop()
