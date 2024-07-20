import os
import sqlite3
import pandas as pd
from datetime import datetime


def add_tables(link):
    csv_folder_path = 'extracted'

    conn = sqlite3.connect(link)
    cursor = conn.cursor()

    for filename in os.listdir(csv_folder_path):
        if filename.endswith('.csv'):
                
            csv_file_path = os.path.join(csv_folder_path, filename)

            df = pd.read_csv(csv_file_path)
                
            # Filter data for today and future dates
            df['date'] = pd.to_datetime(df['date'])
            today = datetime.today().strftime(r'%Y-%m-%d')
            df = df[df['date'] >= today]
                
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS data (
                    date TEXT,
                    hour INTEGER,
                    temp REAL,
                    dwpt REAL,
                    rhum INTEGER,
                    prcp REAL,
                    snow INTEGER,
                    wdir INTEGER,
                    wspd REAL,
                    wpgt REAL,
                    pres REAL,
                    tsun INTEGER,
                    coco TEXT,
                    station TEXT
                )
            """)
                
            df.to_sql('data', conn, if_exists='append', index=False)

    conn.commit()
    conn.close()

