import pandas as pd
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import bikeshare_2 as bs


def get_users_insights(df):

    user_ct, cust_ct, subs_ct = {}, {}, {}

    for day in bs.DAYS:
        dayframe = df[df['day_of_week'] == day]
        user_ct[day] = dayframe['day_of_week'].count()

        cust_frame = dayframe[dayframe['User Type'] == 'Customer']
        cust_ct[day] = cust_frame['User Type'].count()

        subs_frame = dayframe[dayframe['User Type'] == 'Subscriber']
        subs_ct[day] = subs_frame['User Type'].count()

    plot = dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=list(cust_ct.keys()),
                    y=list(cust_ct.values()),
                    name='Customer',
                    marker=go.bar.Marker(
                        color='rgb(55, 83, 109)'
                    )
                ),
                go.Bar(
                    x=list(subs_ct.keys()),
                    y=list(subs_ct.values()),
                    name='Subscriber',
                    marker=go.bar.Marker(
                        color='rgb(26, 118, 255)'
                    )
                )
            ],
            layout=go.Layout(
                title='User counts on days of the week',
                showlegend=True,
                legend=go.layout.Legend(
                    x=0,
                    y=1
                ),
                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
            )
        ),
        style={'height': 300},
        id='user-stats'
    )
    return plot
