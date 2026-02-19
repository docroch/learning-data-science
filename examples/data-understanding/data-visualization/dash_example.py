import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import os

app = Dash(__name__)

dataset = os.path.join("datasets", "EPA_fuel_economy_summary.csv")
df = pd.read_csv("EPA_fuel_economy_summary.csv")

fig = px.histogram(
    df,
    x='fuelCost08',
    color='class_summary',
    labels={'fuelCost08': 'Annual Fuel Cost'},
    nbins=40,
    title='Fuel Cost Distribution'
)

app.layout = html.Div(children=[
    html.H1('داده های مصرف انرژی اتومبیل ها'),
    html.Div('سالیانه'),
    dcc.Graph(id='example-histogram', figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)