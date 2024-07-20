import shutil
import os
from src.dataExtractor import extract_stations
from src.downloader import download_stations
from src.unarchivator import unarchive
from src.headers import set_headers
from src.script import add_tables

#UERP0

if __name__ == "__main__":
    try: 
        shutil.rmtree('archives')
        shutil.rmtree('extracted')
    except Exception: pass 

    a = input()
    
    os.mkdir('archives')
    os.mkdir('extracted')
    download_stations(a)
    extract_stations(a)
    unarchive(a)
    set_headers()
    add_tables(a)

    try: 
        shutil.rmtree('archives')
        shutil.rmtree('extracted')
    except Exception: pass 


