import bikeshare_2 as bs
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# Loading the dataframe
df = bs.load_data('chicago', 'all', 'all')


print('-'*80)
df.sort_values('Trip Duration', axis=0, ascending=True, inplace=True)
print(df.head(2))

hf = df.tail(10)
x = hf['routes']
y = hf['Trip Duration']/3600


# Graph configuration
app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Data Visualization with Dash'),
    html.Div(children='''
        Chart1        
    '''),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Line(
                    x=x,
                    y=y,
                    name='Trip Durations',
                    marker=go.Marker(
                        color='rgb(55, 83, 109)'
                    )
                )
            ],
            layout=go.Layout(
                title='Top trip durations. ',
                showlegend=True,
                legend=go.Legend(
                    x=0,
                    y=1
                ),
                margin=go.Margin(l=40, r=0, t=40, b=30)
            )
        ),
        style={'height': 300},
        id='my-graph'
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
