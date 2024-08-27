import pyodbc

# Настройки подключения
server = 'Server2008'  # Имя сервера или IP-адрес
database = 'faraon_test'    # Имя базы данных
username = 'МашонкинВР'    # Имя пользователя
password = '250269'    # Пароль

# Создаем строку подключения
connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Устанавливаем соединение с базой данных
    connection = pyodbc.connect(connection_string)

    # Создаем курсор
    cursor = connection.cursor()

    # Выполняем запрос
    cursor.execute("SELECT @@VERSION;")

    # Получаем результат
    row = cursor.fetchone()
    while row:
        print(row[0])
        row = cursor.fetchone()

    # Закрываем соединение
    cursor.close()
    connection.close()

except pyodbc.Error as e:
    print(f"Ошибка подключения к базе данных: {e}")
