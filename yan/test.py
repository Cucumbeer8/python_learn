import sqlite3

# Имя новой базы данных
database_name = 'yan.db'

# Имя файла с SQL-скриптом
sql_script_file = 'backupdatabase.sql'

# Создаем новое соединение с базой данных
conn = sqlite3.connect(database_name)
cursor = conn.cursor()

# Читаем SQL-скрипт из файла
with open(sql_script_file, 'r') as file:
    sql_script = file.read()

# Выполняем SQL-скрипт
try:
    cursor.executescript(sql_script)
    print(f"База данных '{database_name}' успешно создана и загружена из '{sql_script_file}'")
except sqlite3.Error as e:
    print(f"Ошибка при выполнении SQL-скрипта: {e}")
finally:
    # Закрываем соединение с базой данных
    conn.close()
