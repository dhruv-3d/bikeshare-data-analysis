import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

import bikeshare_2 as bs
import user_counts_by_day as ucd
import popular_hours as ph
import range_slider as rs
import common_stats as cs


# Load the data
df = bs.load_data(city='chicago', month='all', day='all')
user_stat = bs.user_stats(df)
print('-'*40)

# Graph configuration
app = dash.Dash(__name__)
server = app.server
app.layout = html.Div(children=[
    html.H1(
        children='Exploring US Bikeshare Data',
        style={'text-align': 'center'}
    ),

    html.H3("Bikeshare System:"),
    html.Span(children=[
        "Over the past decade, bicycle-sharing systems have been growing in\
        number and popularity in cities across the world. Bicycle-sharing systems\
        allow users to rent bicycles on a very short-term basis for a price.\
        This allows people to borrow a bike from point A and return it at point B, \
        though they can also return it to the same location if they'd like to just go for a ride."
    ],
        style={'font-size': 18}),

    html.Div(
        children=[
            html.H3('Select city to analyze:'),
            dcc.Dropdown(
                id='city-dropdown',
                options=[
                    {'label': 'Chicago', 'value': 'chicago'},
                    {'label': 'Washington', 'value': 'washington'}
                ],
                value='chicago'
            ),
            html.Span(
                id='hidden-df',
                children=None,
                style={'display': 'None'}
            )
        ],
        style={
            'padding-bottom': '1%',
            'margin-right': '70%'
        }
    ),

    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Station & Trip Stats', children=[
            html.Div(children=[
                html.P(children=[
                    html.Span(
                        'Some more insights regarding bikesharing in '
                    ),
                    html.Span(
                        children=[],
                        id='city-name',
                        style={
                            'text-transform': 'capitalize',
                            'font-weight': 'bold'
                        }
                    ),
                ],
                style={
                    'text-align': 'center',
                    'font-size': 20,
                    'margin-top': 40
                }),
                html.Div(children=cs.other_stats(df),
                id='common-stats',
                style={
                    'font-size': 16,
                    'padding': '40px 0px 0px 0px'
                    }
                )],
            ),
            
        ]),
        dcc.Tab(label='User Insights', children=[
            html.Div(children=[
                html.P(
                    'Describe in breif about the plotting done below.'
                ),
                dcc.Graph(
                    figure=go.Figure(
                        data=ucd.get_users_insights(df),
                        layout=go.Layout(
                            xaxis={'title': 'Days of the week'},
                            yaxis={'title': 'Number of users'},
                            title='User counts on days of the week',
                            showlegend=True,
                            legend=go.layout.Legend(
                                x=0,
                                y=1
                            ),
                            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                        )
                    ),
                    style={
                        'height': 300,
                        'padding': 30,
                    },
                    id='user-stats-graph'
                ),
                html.Div(
                    children=[rs.month_selector('user-month-slider')],
                    style={'padding': 30}
                ),
                html.P(
                    'Total No. of subscribers: ' +
                    str(user_stat['user_counts'][0])
                ),
                html.P(
                    'Total No. of customers: ' +
                    str(user_stat['user_counts'][1])
                ),
                html.P(
                    'Total No. of dependent: ' +
                    str(user_stat['user_counts'][2])
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
                dcc.Graph(
                    figure=go.Figure(
                        data=ph.get_time_insights(df),
                        layout=go.Layout(
                            xaxis={'title': 'Days of the week'},
                            yaxis={
                                'title': 'Popular starting hours (24hr scale)'},
                            title='Comparision of popular starting hours between Subscribers and Customers',
                            showlegend=True,
                            legend=go.layout.Legend(
                                x=0,
                                y=1
                            ),
                            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                        )
                    ),
                    style={
                        'height': 300,
                        'padding': 30,
                    },
                    id='time-stats-graph'
                ),
                html.Div([
                    rs.month_selector('time-month-slider')
                ],
                    style={
                    'padding': 30,
                }),
                html.Hr(),
                html.P(
                    'Describe in detail, the insights from above plot.'
                ),
            ])
        ]),
    ])
])


# Callback to update the User Insights graph on selection of month(s) from Months Slider
@app.callback(
    Output('user-stats-graph', 'figure'),
    [
        Input('city-dropdown', 'value'),
        Input('user-month-slider', 'value')
    ])
def update_user_figure(city, month):
    filtered_df = bs.load_data(city, month, day='all')

    updated_trace = ucd.get_users_insights(filtered_df)

    return {
        'data': updated_trace,
        'layout': go.Layout(
            xaxis={'title': 'Days of the week'},
            yaxis={'title': 'Number of users'},
            title='User counts on days of the week in ' + city.title(),
            showlegend=True,
            legend=go.layout.Legend(
                x=0,
                y=1
            ),
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
        )
    }


# Callback to update the Time Insights graph on selection of month(s) from Months Slider
@app.callback(
    Output('time-stats-graph', 'figure'),
    [
        Input('city-dropdown', 'value'),
        Input('time-month-slider', 'value')
    ])
def update_time_figure(city, month):

    filtered_df = bs.load_data(city, month=month, day='all')

    updated_trace = ph.get_time_insights(filtered_df)

    return {
        'data': updated_trace,
        'layout': go.Layout(
            xaxis={'title': 'Days of the week'},
            yaxis={'title': 'Popular starting hours (24hr scale)'},
            title='Comparision of popular starting hours between Subscribers and Customers in ' + city.title(),
            showlegend=True,
            legend=go.layout.Legend(
                x=0,
                y=1
            ),
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
        )
    }


@app.callback(
    Output('city-name', 'children'),
    [Input('city-dropdown', 'value')])
def selected_city(city):
    return city

@app.callback(
    Output('hidden-df', 'children'),
    [Input('city-dropdown', 'value')])
def load_df(city):
    new_df = bs.load_data(city, month='all', day='all')
    return new_df.to_json()

@app.callback(
    Output('common-stats', 'children'),
    [Input('hidden-df', 'children')])
def load_new_df_data(df):
    return cs.other_stats(pd.read_json(df))


app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# Loading screen CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})


if __name__ == '__main__':
    app.run_server(debug=True)
