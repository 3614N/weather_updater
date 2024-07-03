import os
import pandas as pd

def headers():
    # Путь к папке с CSV файлами
    folder_path = 'csv'

    # Заголовки, которые нужно добавить
    headers = ['date', 'tavg', 'tmin', 'tmax', 'prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun']

    # Проход по всем файлам в указанной папке
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            
            # Чтение данных из файла без заголовков
            df = pd.read_csv(file_path, header=None)
            
            # Добавление заголовков
            df.columns = headers
            
            # Сохранение файла с новыми заголовками
            df.to_csv(file_path, index=False)

    print('Заголовки успешно добавлены ко всем CSV файлам в папке.')
