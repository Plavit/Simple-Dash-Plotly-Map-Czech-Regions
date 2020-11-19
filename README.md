# Simple-Dash-Plotly-Map-Czech-Regions
A simple Dash Plotly map with a custom GeoJSON of Czech administrative subdvisions

## Description
I was asked to create a simple chloropleth map of Czech administrative regions (kraje). This was not simple, as the basic chloropleth map implemented in Dash was really bugging out from the data, was coloring in wrong parts of the map and was thus unusable. Therefore, I went with the Mapbox implementation, which works fine. I also created three levels of detail of the GeoJSON.

## Credits
GeoJSON was adapted from https://github.com/JirkaChadima/cz-region-boundaries and simplified
