import gzip
import shutil
import os
import time


def unarchive(a):
    source_folder = 'archives'
    destination_folder = 'extracted'

    # Создаем целевую папку, если она не существует
    os.makedirs(destination_folder, exist_ok=True)

    # Проходим по всем файлам в папке source_folder
    if a == "all":
        for filename in os.listdir(source_folder):
            if filename.endswith('.gz'):
                source_path = os.path.join(source_folder, filename)
                destination_path = os.path.join(destination_folder, filename[:-3])  # Убираем .gz из имени файла

                with gzip.open(source_path, 'rb') as f_in:
                    with open(destination_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
    else:
        while   f"{a}.csv.gz" not in os.listdir(source_folder): pass

        for filename in os.listdir(source_folder):
            if filename.endswith('.gz'):
                source_path = os.path.join(source_folder, filename)
                destination_path = os.path.join(destination_folder, filename[:-3])  # Убираем .gz из имени файла

                with gzip.open(source_path, 'rb') as f_in:
                    with open(destination_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
            
    print("Все файлы успешно распакованы.")
