import dash_core_components as dcc
import dash_html_components as html
import bikeshare_2 as bs


def other_stats(df):

    station_stat = bs.station_stats(df)
    time_stat = bs.time_stats(df)

    html.Div(children=[
        html.P(
            'Popular month'
        )        
    ])

    return smthin
