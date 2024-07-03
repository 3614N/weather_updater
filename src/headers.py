import os
import pandas as pd

def set_headers():
    folder_path = 'extracted'

    headers = ['date', 'tavg', 'tmin', 'tmax', 'prcp', 'snow', 'wdir', 'wspd', 'wpgt', 'pres', 'tsun']

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            
            df = pd.read_csv(file_path, header=None)
            
            df.columns = headers
            
            df.to_csv(file_path, index=False)

    print('Заголовки успешно добавлены ко всем CSV файлам в папке.')
