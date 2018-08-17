import pandas as pd
import numpy as np
import plotly.graph_objs as go

import bikeshare_2 as bs


def get_time_insights(df):

    pop_cust_hour, pop_subs_hour, pop_hour = {}, {}, {}
    for day in bs.DAYS:
        dayframe = df[df['day_of_week'] == day]
        # pop_hour[day] = dayframe['hour'].mode()[0]

        cust_frame = dayframe[dayframe['User Type'] == 'Customer']
        pop_cust_hour[day] = cust_frame['hour'].mode()[0]

        subs_frame = dayframe[dayframe['User Type'] == 'Subscriber']
        pop_subs_hour[day] = subs_frame['hour'].mode()[0]

    traces = [
        go.Line(
            x=list(pop_cust_hour.keys()),
            y=list(pop_cust_hour.values()),
            name='Customer',
            marker=go.scatter.Marker(
                color='rgb(55, 83, 109)'
            )
        ),
        go.Line(
            x=list(pop_subs_hour.keys()),
            y=list(pop_subs_hour.values()),
            name='Subscriber',
            marker=go.scatter.Marker(
                color='rgb(26, 118, 255)'
            )
        )
    ]

    return traces
