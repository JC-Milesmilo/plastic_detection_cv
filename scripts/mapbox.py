import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 
import plotly.io as pio
pio.renderers.default = 'browser'


class mapbox():

    def __init__(self):
        return

    
    def get_map(self,df):
        fig = px.density_mapbox(df, lat='latitude', lon='longitude', z='count',
                        mapbox_style="stamen-terrain",radius=5)

        fig.show()

#data=pd.DataFrame(
#    {'latitude': [52.635752,52.635752],
# 'longitude': [-1.143391,-1.143391],
# 'count': [5,6]}
# 
# )