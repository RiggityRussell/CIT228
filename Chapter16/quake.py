import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'Chapter16/json/4.5_week.json'
with open(filename, encoding='utf8') as file:
    quake_data = json.load(file)

readable_file = 'Chapter16/json/readable_week.json'
with open(readable_file, 'w') as file:
    json.dump(quake_data, file, indent=4)

all_eq_dicts = quake_data['features']
#print(len(all_eq_dicts))
mags, longs, lats, = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    longs.append(lon)
    lats.append(lat)

data = [Scattergeo(lon = longs, lat=lats)]
my_layout = Layout(title="Global Earthquakes with a magnitude 4.5 or higher")

fig= {'data' : data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')


#print(sorted(mags))
print(longs)
print(lats)
