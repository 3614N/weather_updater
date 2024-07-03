import os
import sqlite3
import pandas as pd


def convert():
    # Укажите путь к папке с CSV файлами
    csv_folder_path = 'csv'

    # Создание или подключение к базе данных
    conn = sqlite3.connect('stations.db')
    cursor = conn.cursor()

    # Функция для создания таблицы
    def create_table(table_name):
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                date TEXT,
                tavg REAL,
                tmin REAL,
                tmax REAL,
                prcp REAL,
                snow INTEGER,
                wdir INTEGER,
                wspd REAL,
                wpgt REAL,
                pres REAL,
                tsun INTEGER
            )
        """)
        conn.commit()

    # Функция для вставки данных из DataFrame в таблицу
    def insert_data(table_name, df):
        df.to_sql(table_name, conn, if_exists='append', index=False)

    # Обработка каждого CSV файла в папке
    for filename in os.listdir(csv_folder_path):
        if filename.endswith('.csv'):
            table_name = os.path.splitext(filename)[0]  # Использование имени файла в качестве имени таблицы
            
            # Добавление префикса '_' к имени таблицы, если оно начинается с цифры
            if table_name[0].isdigit():
                table_name = f"_{table_name}"
            
            csv_file_path = os.path.join(csv_folder_path, filename)
            
            # Чтение CSV файла в DataFrame
            df = pd.read_csv(csv_file_path)
            
            # Создание таблицы, если она не существует
            create_table(table_name)
            
            # Вставка данных в таблицу
            insert_data(table_name, df)

    # Закрытие соединения с базой данных
    conn.close()
