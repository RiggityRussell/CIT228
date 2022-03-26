import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# file = 'vizualization_project/data/all_month.json'
# with open(file, encoding='utf8') as f:
#     sig_quake = json.load(f)

# readable_file = 'vizualization_project/data/readable_eq_all.json'
# with open(readable_file, 'w') as quakey:
#     json.dump(sig_quake, quakey, indent=4)


file = 'vizualization_project/data/readable_eq_all.json'
with open(file) as f:
    sig_quake = json.load(f)

quakes = sig_quake['features']

mags, description, lon, lat = [], [], [], []
for eq_dict in quakes:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
    place = eq_dict['properties']['place']
    tsunami = eq_dict['properties']['tsunami']
    felt = eq_dict['properties']['felt']
    alert = eq_dict['properties']['alert']
    description.append(f"Location: {place}, tsunami size: {tsunami}, humans effected: {felt}, severity: {alert}")
    lons = eq_dict['geometry']['coordinates'][0]
    lon.append(lons)
    lats = eq_dict['geometry']['coordinates'][1]
    lat.append(lats)
    

data = [{'type': 'scattergeo',
    'lon': lon,
    'lat': lat,
    'text': description, 
    'marker': {
                'size': [8*mag for mag in mags],
                'color': mags,
                'colorscale': 'inferno',
                'reversescale': False,
                'colorbar': {'title': 'Magnitude'}
              }
    }]

my_layout = Layout(title="Global Earthquakes in the last Month")

fig= {'data' : data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

#