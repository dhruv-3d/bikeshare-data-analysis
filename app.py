import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html

import bikeshare_2 as bs
import user_counts_by_day as ucd
import popular_hours as ph

# Load the data
df = bs.load_data(city='chicago', month='all', day='all')
user_stat = bs.user_stats(df)
print('-'*40)
print(user_stat)

# Graph configuration
app = dash.Dash()
app.layout = html.Div(children=[
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='User Insights', children=[
            html.Div([
                html.P(
                    'Describe in breif about the plotting done below.'
                ),
                ucd.get_users_insights(df),
                html.Hr(),
                html.P(
                    'Total No. of subscribers: ' + str(user_stat['user_types'][0])
                ),
                html.P(
                    'Total No. of customers: ' + str(user_stat['user_types'][1])
                ),
                html.P(
                    'Total No. of dependent: ' + str(user_stat['user_types'][2])
                ),
                html.Hr(),
                html.P(
                    'Describe in detail, the insights from above plot.'
                ),
            ])
        ]),
        dcc.Tab(label='Time Insights', children=[
            html.Div([
                html.P(
                    'Describe in breif about the plotting done below.'
                ),
                ph.get_time_insights(df),
                html.Hr(),
                html.P(
                    'Describe in detail, the insights from above plot.'
                ),
            ])
        ]),
        dcc.Tab(label='Tab three', children=[
            html.Div([
                html.H1("This is the content in tab 3"),
            ])
        ]),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
