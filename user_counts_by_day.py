import pandas as pd
import numpy as np
import plotly.graph_objs as go

import bikeshare_2 as bs


def get_users_insights(df):

    user_ct, cust_ct, subs_ct = {}, {}, {}

    for day in bs.DAYS:
        dayframe = df[df['day_of_week'] == day]
        # user_ct[day] = dayframe['day_of_week'].count()

        cust_frame = dayframe[dayframe['User Type'] == 'Customer']
        cust_ct[day] = cust_frame['User Type'].count()

        subs_frame = dayframe[dayframe['User Type'] == 'Subscriber']
        subs_ct[day] = subs_frame['User Type'].count()

    traces = [
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
    ]

    return traces
