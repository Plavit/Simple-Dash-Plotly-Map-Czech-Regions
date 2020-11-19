import pandas as pd
import plotly.express as px
import json

with open('maps/czech-regions-med-res.json', encoding='utf-8') as json_file:
    geojson = json.load(json_file)

df = pd.read_csv('test-data.csv')

# Checking that the data parameter is the same as the geojson parameter
print(df["name-cz"][0])
print(geojson["features"][0]["properties"]["name:cs"])



fig = px.choropleth_mapbox(df, geojson=geojson, locations='name-cz', featureidkey="properties.name:cs", color='num',
                           color_continuous_scale="plasma",
                           range_color=(0, 12),
                           labels={'num': 'Náhodná proměnná'},
                           mapbox_style="carto-positron",
                           zoom=7, center={"lat": 50, "lon": 15},
                           )

fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig.show()
