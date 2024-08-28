import tkinter as tk

def on_submit():
    user_input1 = entry1.get()
    user_input2 = entry2.get()
    user_input3 = entry3.get()
    print("Введено:", user_input1, user_input2, user_input3)

    # Получаем количество колонок и строк
    columns, rows = root.grid_size()
    print(f"Количество колонок: {columns}, Количество строк: {rows}")

    # Просматриваем всех виджетов в сетке и выводим информацию о них
    for widget in root.grid_slaves():
        info = widget.grid_info()
        print(f"Виджет: {widget}, Строка: {info['row']}, Колонка: {info['column']}")

# Создаем главное окно
root = tk.Tk()
root.title("Пример работы с сеткой")

# Создаем метки и поля ввода с выравниванием по сетке (grid)
label1 = tk.Label(root, text="Короткое имя:")
label1.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

entry1 = tk.Entry(root, width=30)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Очень длинное имя поля:")
label2.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

entry2 = tk.Entry(root, width=30)
entry2.grid(row=1, column=1, padx=5, pady=5)

label3 = tk.Label(root, text="Среднее имя:")
label3.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

entry3 = tk.Entry(root, width=30)
entry3.grid(row=2, column=1, padx=5, pady=5)

# Устанавливаем фокус на первое поле ввода при запуске формы
entry1.focus()

# Кнопка для отправки данных с фиксированным размером и выравниванием по правому краю
submit_button = tk.Button(root, text="Отправить", command=on_submit, width=15, height=2)
submit_button.grid(row=3, column=1, sticky=tk.E, padx=5, pady=10)

# Запускаем главное окно
root.mainloop()
