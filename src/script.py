import os
import sqlite3
import pandas as pd


def add_tables(a : str):
    if a == "all":
        csv_folder_path = 'extracted'

        conn = sqlite3.connect('stations.db')
        cursor = conn.cursor()

        for filename in os.listdir(csv_folder_path):
            if filename.endswith('.csv'):
                table_name = os.path.splitext(filename)[0] 
                
                if table_name[0].isdigit():
                    table_name = f"_{table_name}"
                
                csv_file_path = os.path.join(csv_folder_path, filename)
                
                df = pd.read_csv(csv_file_path)
                
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
                
        df.to_sql(table_name, conn, if_exists='append', index=False)

        conn.close()
    else:
        csv_folder_path = 'extracted'

        conn = sqlite3.connect('stations.db')
        cursor = conn.cursor()

        for filename in os.listdir(csv_folder_path):
            if filename.endswith('.csv'):
                table_name = os.path.splitext(filename)[0] 
                
                if table_name[0].isdigit():
                    table_name = f"_{table_name}"
                
                csv_file_path = os.path.join(csv_folder_path, filename)
                
                df = pd.read_csv(csv_file_path)
                
                cursor.execute(f"DROP TABLE {a}")
                conn.commit()

                cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {a} (
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
                
        df.to_sql(table_name, conn, if_exists='append', index=False)
        
        conn.close()
