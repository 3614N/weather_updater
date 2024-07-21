import folium
from branca.colormap import linear

def map_constructor_temp(lat, lon, square_data, square_corners):
    map_object = folium.Map(location=[lat, lon], zoom_start=15)

    temp_values = [data[1]['temp'] for data in square_data]
    min_temp = min(temp_values)
    max_temp = max(temp_values)
    colormap = linear.YlOrRd_09.scale(min_temp, max_temp)

    for i, part in enumerate(square_corners):
        rec_bounds = [part[0], part[2]]
        temp_value = square_data[i][1]['temp']
        color = colormap(temp_value)

        folium.Rectangle(
            bounds=rec_bounds,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            popup=f"Temp: {temp_value}"
        ).add_to(map_object)

    map_object.save('map_temp.html')

def map_constructor_rhum(lat, lon, square_data, square_corners):
    map_object = folium.Map(location=[lat, lon], zoom_start=15)

    rhum_values = [data[1]['rhum'] for data in square_data]
    min_rhum = min(rhum_values)
    max_rhum = max(rhum_values)
    colormap = linear.YlGn_09.scale(min_rhum, max_rhum)

    for i, part in enumerate(square_corners):
        rec_bounds = [part[0], part[2]]
        rhum_value = square_data[i][1]['rhum']
        color = colormap(rhum_value)

        folium.Rectangle(
            bounds=rec_bounds,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            popup=f"Humidity: {rhum_value}"
        ).add_to(map_object)

    map_object.save('map_rhum.html')

def map_constructor_pres(lat, lon, square_data, square_corners):
    map_object = folium.Map(location=[lat, lon], zoom_start=15)

    pres_values = [data[1]['pres'] for data in square_data]
    min_pres = min(pres_values)
    max_pres = max(pres_values)
    colormap = linear.Spectral_09.scale(min_pres, max_pres)

    for i, part in enumerate(square_corners):
        rec_bounds = [part[0], part[2]]
        pres_value = square_data[i][1]['pres']
        color = colormap(pres_value)

        folium.Rectangle(
            bounds=rec_bounds,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            popup=f"Pressure: {pres_value}"
        ).add_to(map_object)

    map_object.save('map_pres.html')