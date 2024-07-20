import webbrowser
import shutil


def download_stations():
    webbrowser.open("https://github.com/meteostat/weather-stations/raw/master/stations.db", new=0, autoraise=True)
    while True:
        try:
            shutil.move("archives/stations.db", "../forecasts.db")
            break
        except Exception:
            pass
