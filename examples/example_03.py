import tkinter as tk
from tkinter import messagebox

def submit_data(event=None):
    user_input = entry.get()
    if user_input.strip() == "":
        messagebox.showwarning("Внимание", "Поле ввода не должно быть пустым!")
    else:
        result_label.config(text=f"Вы ввели: {user_input}")
        entry.delete(0, tk.END)  # Очищаем поле ввода

def toggle_fullscreen(event=None):
    global fullscreen  # Используем глобальную переменную для отслеживания режима
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)

# Создаем главное окно
root = tk.Tk()
root.title("Пример ввода данных")

# Получаем размеры экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Устанавливаем окно на полный экран
# fullscreen = True
# root.attributes("-fullscreen", fullscreen)

root.geometry(f"{screen_width}x{screen_height}")

# Привязываем обработчик события нажатия клавиши "Esc"
root.bind("<Escape>", toggle_fullscreen)

# Создаем метку для инструкций
instruction_label = tk.Label(root, text="Введите что-нибудь:")
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
