import webbrowser
import shutil

def download_stations():
    webbrowser.open("https://github.com/meteostat/weather-stations/raw/master/stations.db", new=0, autoraise=True)

    while True:
        try:
            shutil.move("D:/Repositories/weather_updater/archives/stations.db", "D:/Repositories/weather_updater/")
            break
        except Exception:pass
