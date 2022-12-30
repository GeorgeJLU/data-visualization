import plotly.express as px
import pandas as pd

from eq_explore_data import lons
from eq_explore_data import lats
from eq_explore_data import titles
from eq_explore_data import mags

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags),
    columns=["经度", "纬度", "位置", "震级"]
    )
data.head()

# 直接利用散点图绘图太粗暴
# fig = px.scatter(
#     x=lons,
#     y=lats,
#     labels={'x':"经度", 'y':"纬度"},
#     range_x=[-200, 200],
#     range_y=[-90, 90],
#     width=800,
#     height=800,
#     title="全球地震散点图",
#     size="震级",
#     size_max=10,
#     color="震级",
#     )

fig = px.density_mapbox(
    data,
    lon="经度",
    lat="纬度",
    z="震级",
    hover_name="位置",
    radius=5,
    center=dict(lon=180, lat=0),
    zoom=0,
    mapbox_style="stamen-terrain"
    )

fig.write_html("result/global_earthquakes.html")
fig.show()