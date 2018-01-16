import pandas
import folium

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name_vol = list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif 1000<= elevation <3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58,-99.09], zoom_start = 6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lati, longi, vol, el in zip(lat, lon, name_vol, elev):
   # fg.add_child(folium.Marker(location=[lati, longi], popup=folium.Popup("Volcano " +vol +", Elevation: " +str(el) +" m", parse_html=True), icon = folium.Icon(color=color_producer(el))))
    fgv.add_child(folium.CircleMarker(location=[lati, longi], popup=folium.Popup("Volcano " +vol +", Elevation: " +str(el) +" m", parse_html=True), fill= True, fill_color=color_producer(el), fill_opacity=1, color = "white", radius= 10))

fgp = folium.FeatureGroup(name="Population")

#Using the data from world.json we made boundries using the coordinates
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding= "utf-8-sig").read(),
                            style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005']< 10000000
                            else 'orange' if 10000000<= x['properties']['POP2005'] < 50000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")