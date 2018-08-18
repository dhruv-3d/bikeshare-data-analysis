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
app.title = 'Exploring Bikeshare Data'
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
                    {'label': 'New York', 'value': 'new york city'},
                    {'label': 'Washington', 'value': 'washington'}
                ],
                value='chicago'
            ),
        ],
        style={
            'padding-bottom': '1%',
            'margin-right': '70%'
        }
    ),

    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Common', children=[
            html.Div(children=[
                html.H4(
                    children='Some common insights of all the cites',
                ),
                html.Div(children=cs.other_stats()[0]),
                html.Hr(),
                html.Div(children=cs.other_stats()[1]),
            ],
                style={
                    'padding-bottom': 50,
                    'text-align': 'center',
                    'align-items': 'center'
            }),
        ]),
        dcc.Tab(label='User Insights', children=[
            html.Div(children=[
                html.P(
                    "The below graph shows the data of number of different types of\
                     bikesharing users i.e. Subscribers and Customers over\
                     the days of the week. By defualt it shows data for the\
                     span of all the 6 months, but if you want you can use\
                     the range slider below the graph to check the data for\
                     particular month or range of month. The graph is interactive,\
                     you can hover over the plotted data and see the labels\
                     and values. If you want to check for particular type of user,\
                     you can just toggle the graph legends. Aside from this the graph\
                     have a default toolbar which appears on hover, you can use to play\
                     around if you want.",

                    style={'padding': 20, 'font-size': 18}
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
                        'padding': 20,
                    },
                    id='user-stats-graph'
                ),
                html.Div(
                    children=[rs.month_selector('user-month-slider')],
                    style={'padding': 20}
                ),
                html.Hr(),
                html.Div(children=[
                    html.P(
                        "Aside from the common statistics gained from the data\
                         which is mentioned in 'Common' tab, the above graph\
                         reveals some other insights."
                    ),
                    html.P(html.Ul(html.Li(children=[
                        "You can see that for all the months, overall the number\
                         of Subscribers remains high during weekdays and low on\
                         weekends and vice versa for the Customers."
                    ]))),
                    html.P(html.Ul(html.Li(children=[
                        "You can see that for all the months, overall the number\
                         of Subscribers remains high during weekdays and low on\
                         weekends and vice versa for the Customers. From that we\
                         can assume that majority of subscribers are people who uses\
                         bikesharing system for their daily commuting and the\
                         "
                    ]))),
                ],
                id='chicago-stats',
                style={'padding': 20, 'font-size': 18, 'display':'block'}),
                html.P(
                    "Throw some new york's insights here for above graph",
                    id='new-york-stats',
                    style={'padding': 20, 'font-size': 18}
                ),
                html.P(
                    "Throw some washington's here for above graph",
                    id='washington-stats',
                    style={'padding': 20, 'font-size': 18}
                ),
            ])
        ]),
        dcc.Tab(label='Time Insights', children=[
            html.Div([
                html.P(
                    "The below graph shows the data of popular hours of the\
                     day which different types of bikesharing users i.e.\
                     Subscribers and Customers are most active for every\
                     days of the week. By defualt it shows data for the\
                     span of all the 6 months, but if you want you can use\
                     the range slider below the graph to check the data for\
                     particular month or range of month. The graph is interactive,\
                     you can hover over the plotted data and see the labels\
                     and values. If you want to check for particular type of user,\
                     you can just toggle the graph legends. Aside from this the graph\
                     have a default toolbar which appears on hover, you can use to play\
                     around if you want.",

                    style={'padding': 20, 'font-size': 18}
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
                        'padding': 20,
                    },
                    id='time-stats-graph'
                ),
                html.Div([
                    rs.month_selector('time-month-slider')
                ],
                    style={
                    'padding': 20,
                }),
                html.Hr(),
                html.P(
                    'Describe in detail, the insights from above plot.'
                ),
            ])
        ]),
    ]),
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
    Output('chicago-stats', 'style'),
    [Input('city-dropdown', 'value')])
def hide_show(city):
    if city == 'chicago':
        return {'padding': 20, 'font-size': 18, 'display':'block'}
    else:
        return {'display': 'none'}


@app.callback(
    Output('new-york-stats', 'style'),
    [Input('city-dropdown', 'value')])
def hide_show(city):
    if city == 'new york city':
        return {'padding': 20, 'font-size': 18, 'display':'block'}
    else:
        return {'display': 'none'}


@app.callback(
    Output('washington-stats', 'style'),
    [Input('city-dropdown', 'value')])
def hide_show(city):
    if city == 'washington':
        return {'padding': 20, 'font-size': 18, 'display':'block'}
    else:
        return {'display': 'none'}


app.css.append_css(
    {"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
# Loading screen CSS
app.css.append_css(
    {"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})


if __name__ == '__main__':
    app.run_server(debug=True)
