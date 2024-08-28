import tkinter as tk
from tkinter import messagebox

def submit_data(event=None):
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
root.title("Авторизация пользователя")


# Получаем размеры экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Устанавливаем размеры окна
root.geometry(f"{screen_width}x{screen_height}")


# Создаем метку для инструкций
instruction_label = tk.Label(root, text="Пользователь:")
instruction_label.pack(pady=10)

# Создаем поле ввода
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Привязываем обработчик события нажатия клавиши "Enter"
entry.bind("<Return>", submit_data)

# Создаем метку для отображения результата
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Запускаем главное окно
root.mainloop()
