import pg8000.native

SUPERUSER = "pguser"
SUPERUSER_PASSWORD = "pwd123"
DB_HOST = "localhost"
DB_PORT = 8082

#Чтобы назначить другого владельца базы данных необходимо создать роль( CREATE ROLE)
DB_OWNER = "pguser"
DB_NAME = input("Database name: ")
DB_PASSWORD = input("Database password: ")


def initialize_database():
    try:
        # Подключаемся к базе данных postgres как суперпользователь
        connection = pg8000.native.Connection(
            user=SUPERUSER, password=SUPERUSER_PASSWORD, host=DB_HOST,
            port=DB_PORT, database="pgdb1"
        )

        # Создаем базу данных
        connection.run(f"CREATE DATABASE {DB_NAME} OWNER {DB_OWNER};")
        print(f"База данных '{DB_NAME}' успешно создана с владельцем '{DB_OWNER}'.")

    except pg8000.exceptions.DatabaseError as e:
        print(f"Ошибка при создании базы данных: {e}")
    except Exception as e:
        print(f"Общая ошибка: {e}")
    finally:
        # Закрываем соединение
        try:
            connection.close()
        except Exception:
            pass


if __name__ == "__main__":
    initialize_database()
