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
pop_cust_hour, pop_subs_hour = {}, {}
xc, yc, xs, ys = [], [], [], []

for day in days:
    dayframe = df[df['day_of_week'] == day]

    cust_frame = dayframe[dayframe['User Type'] == 'Customer']
    pop_cust_hour[day] = cust_frame['hour'].mode()[0]

    subs_frame = dayframe[dayframe['User Type'] == 'Subscriber']
    pop_subs_hour[day] = subs_frame['hour'].mode()[0]

for day, ph in pop_cust_hour.items():
    xc.append(day)
    yc.append(ph)

for day, ph in pop_subs_hour.items():
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
                go.Line(
                    x=xc,
                    y=yc,
                    name='Customer',
                    marker=go.Marker(
                        color='rgb(55, 83, 109)'
                    )
                ),
                go.Line(
                    x=xs,
                    y=ys,
                    name='Subscriber',
                    marker=go.Marker(
                        color='rgb(26, 118, 255)'
                    )
                )
            ],
            layout=go.Layout(
                title='Comparision of popular starting hours between Subscribers and Customers',
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
