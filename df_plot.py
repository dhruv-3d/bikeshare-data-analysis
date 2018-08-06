import bikeshare_2 as bs
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# Loading the dataframe
df = bs.load_data('chicago', 'all', 'all')

days = df['day_of_week'].unique()

for day in days:
    data[day]['cust_count'] = df[(df['User Type'] == 'Customer') & (df['day_of_week'] == day)]['Trip Duration']


data = {
    'Sunday': {
        'subs_count': 100,
        'cust_count': 200,
    },
    'Monday': {
        'subs_count': 150,
        'cust_count': 210
    }
}

subs_count = data['Sunday']['subs_count'] + data['Monday']['subs_count']
cust_count = data['Sunday']['cust_count'] + data['Monday']['cust_count']

# customers = {}
# subscribers = {}

# for day in df['day_of_week'].unique():
#     customers[day] = df[(df['User Type'] == 'Customer') & (df['day_of_week'] == day)]['Trip Duration']
#     subscribers[day] = df[(df['User Type'] == 'Subscriber') & (df['day_of_week'] == day)]['Trip Duration']

# customers = df[(df['User Type'] == 'Customer') & (df['day_of_week'] == 'Sunday')][['Trip Duration', 'day_of_week']].values
# subscriber = df[(df['User Type'] == 'Subscriber') & (df['day_of_week'] == 'Sunday')]['Trip Duration'].values
# day_of_week = df['day_of_week'].unique()


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
                    x=list(data.keys()),
                    y=[data['Sunday']['cust_count'], data['Monday']['cust_count']],
                    name='Customer',
                    marker=go.Marker(
                        color='rgb(55, 83, 109)'
                    )
                ),
                go.Bar(
                    x=list(data.keys()),
                    y=[data['Sunday']['subs_count'], data['Monday']['subs_count']],
                    name='subscriber',
                    marker=go.Marker(
                        color='rgb(26, 118, 255)'
                    )
                )
            ],
            layout=go.Layout(
                title='Demo',
                showlegend=True,
                legend=go.Legend(
                    x=0,
                    y=1.0
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
