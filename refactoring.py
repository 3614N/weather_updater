import sqlite3
import pandas as pd

# Подключение к базе данных
conn = sqlite3.connect('stations.db')

# Получение списка всех таблиц
tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(tables_query, conn)['name'].tolist()

# Исключение ненужных таблиц
excluded_tables = {'identifiers', 'inventory', 'names', 'stations'}
tables_to_include = [table for table in tables if table not in excluded_tables]

# Чтение данных из таблицы stations
stations_df = pd.read_sql('SELECT * FROM stations', conn)

# Объединение всех таблиц
all_data = []

for table in tables_to_include:
    table_df = pd.read_sql(f'SELECT * FROM {table}', conn)
    
    # Добавление столбца name
    table_df['name'] = table
    table_df['name'] = table_df['name'].apply(lambda x: x.lstrip('_'))
    
    # Добавление столбцов latitude и longitude
    merged_df = pd.merge(table_df, stations_df[['id', 'latitude', 'longitude']], 
                         left_on='name', right_on='id', how='left')
    
    # Добавление в общий список
    all_data.append(merged_df)

# Объединение всех DataFrame в один
result_df = pd.concat(all_data, ignore_index=True)

# Сортировка по столбцу date
result_df = result_df.sort_values(by='date')

# Сохранение результата в CSV файл
result_df.to_csv('data.csv', index=False)

# Закрытие соединения с базой данных
conn.close()

# Вывод сообщения о завершении
print("Результат сохранен в файл 'data.csv'")
