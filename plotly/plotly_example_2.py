'''
https://medium.com/@twelsh37/further-adventures-in-plotly-sankey-diagrams-fdba9ff08af6
just me messing around trying to learn this
'''

import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.write_html('first_figure.html', auto_open=True)
