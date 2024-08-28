import psycopg2

connection = None  # Инициализируем переменную connection

try:
    connection = psycopg2.connect(
        dbname="test",
        user="Test",
        password="Test1234+",
        host="192.168.3.2",
        port="5432"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("Вы подключены к базе данных - ", db_version)

except Exception as error:
    print("Ошибка при подключении к PostgreSQL:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
