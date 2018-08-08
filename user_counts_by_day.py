import bikeshare_2 as bs
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# Loading the dataframe
df = bs.load_data('chicago', 'all', 'all')

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
user_ct, cust_ct, subs_ct = {}, {}, {}
# x, y = [], []
xc, yc, xs, ys = [], [], [], []

for day in days:
    dayframe = df[df['day_of_week'] == day]
    user_ct[day] = dayframe['day_of_week'].count()

    cust_frame = dayframe[dayframe['User Type'] == 'Customer']
    cust_ct[day] = cust_frame['User Type'].count()
    
    subs_frame = dayframe[dayframe['User Type'] == 'Subscriber']
    subs_ct[day] = subs_frame['User Type'].count()

for day, count in cust_ct.items():
    xc.append(day)
    yc.append(count)

for day, ph in subs_ct.items():
    xs.append(day)
    ys.append(ph)

# Graph configuration
app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Data Visualization with Dash'),

    html.Div(children='''
        
    '''),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=xc,
                    y=yc,
                    name='Customer',
                    marker=go.Marker(
                        color='rgb(55, 83, 109)'
                    )
                ),
                go.Bar(
                    x=xs,
                    y=ys,
                    name='Subscriber',
                    marker=go.Marker(
                        color='rgb(26, 118, 255)'
                    )
                )
            ],
            layout=go.Layout(
                title='User counts on days of the week',
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
