import bikeshare_2 as bs
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html


# load the dataframe
# city, month, day = bs.get_filters()
df = bs.load_data('chicago', 'all', 'all')

hf = pd.DataFrame({
    'Trip Duration': df['Trip Duration'],
    'routes': df['routes']
})

hf['Trip Duration'] = hf['Trip Duration']/60
hf = hf.groupby(['routes'])['Trip Duration'].sum()

hf = hf.tail(100)
x_vals = hf.index
y_vals = hf.values

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Exploring Bikeshare Data'),

    html.Div(children='''
        A visualization of Bike's Trip Duration(in minutes) from 'Start Station' to 'End Station'
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {
                    'x': x_vals,
                    'y': y_vals,
                    'type': 'bar',
                    'name': 'SF'
                },
            ],
            'layout': {
                'title': 'Trip Duration Visualization',
                'yaxis': {'label':'Trip Duration (Minutes)'},
                'xaxis': {'label' :'Start to End stations'},
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)