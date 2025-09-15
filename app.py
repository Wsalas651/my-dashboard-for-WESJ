import os
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Example data
df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 5, 8, 12]})
fig = px.line(df, x='x', y='y', title='Dash Example')

app = Dash(__name__)
server = app.server  # exposes the WSGI app for Gunicorn

app.layout = html.Div([
    html.H1('Dash - Demo'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8050)))
