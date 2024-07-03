import shutil
import os
from src.dataExtractor import extract_stations
from src.downloader import download_stations
from src.unarchivator import unarchive
from src.headers import set_headers
from src.script import add_tables


if __name__ == "__main__":
    try: 
        shutil.rmtree('archives')
        shutil.rmtree('extracted')
        os.remove('stations.db')
    except Exception: pass 
    os.mkdir('archives')
    os.mkdir('extracted')
    download_stations()
    extract_stations()
    unarchive()
    set_headers()
    add_tables()
    try: 
        shutil.rmtree('archives')
        shutil.rmtree('extracted')
    except Exception: pass 


