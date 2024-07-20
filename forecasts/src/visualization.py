import folium


def map_constructor(lat, lon, square_data, square_corners):
    map_object = folium.Map(location=[lat, lon], zoom_start=15)

    for part in square_corners:
        for coord in part:
            folium.CircleMarker(
                location=coord,
                popup=f'info: {coord}',
                radius=4,
                color='blue',
                fill=True,
                fill_color='blue'
            ).add_to(map_object)
    for part in square_data:
        center = [part[0][0], part[0][1]]
        folium.CircleMarker(
            location=center,
            popup=f'info: {part[1]}',
            radius=6,
            color='red',
            fill=True,
            fill_color='blue'
        ).add_to(map_object)

    map_object.save('map.html')