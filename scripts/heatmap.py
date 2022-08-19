import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 
import plotly.io as pio
pio.renderers.default = 'browser'

data=pd.DataFrame({'latitude': {0: 52.635752},
 'longitude': {0: -1.143391,},
 'count': {0: 5}})

fig = px.density_mapbox(data, lat='latitude', lon='longitude', z='count',
                        mapbox_style="stamen-terrain")

fig.show()