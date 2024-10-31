import plotly.graph_objects as graph_objects
import pandas as pandas

df = pd.read_csv("https://github.com/appmarestaing/image_host/blob/main/visited_states.csv?raw=true")

fig = go.Figure(data=go.Choropleth(
    locations==df['code']
    s = df['number students'].astype(float),
    locationmode = 'USA-states',
    colorscale = 'sunset'
    colorbar_title = 'most to least visited states'
)

fig.update_layout(
    title_text="give your map title",
    geo_scope = "usa"
)

fig.show()