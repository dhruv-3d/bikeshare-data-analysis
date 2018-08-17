import dash_core_components as dcc
import dash_html_components as html
import bikeshare_2 as bs


def other_stats():
    all_df = {}
    all_df['chicago'] = bs.load_data('chicago', 'all', 'all')
    all_df['new york'] = bs.load_data('new york city', 'all', 'all')
    all_df['washington'] = bs.load_data('washington', 'all', 'all')

    all_stats = {}
    tr_array, td_array, usr_tr, time_tr = [], [], [], []
    for name, df in zip(all_df.keys(), all_df.values()):
        all_stats[name + '_time_stat'] = bs.time_stats(df)
        all_stats[name + '_user_stat'] = bs.user_stats(df)
        all_stats[name + '_station_stat'] = bs.station_stats(df)
        all_stats[name + '_trip_stat'] = bs.trip_duration_stats(df)


        td_array.append(html.Td(name))
        td_array.append(
            html.Td(all_stats[name + '_user_stat']['user_counts'][0]))
        td_array.append(
            html.Td(all_stats[name + '_user_stat']['user_counts'][1]))

        td_array.append(
            html.Td(all_stats[name + '_time_stat']['popular_month']))
        td_array.append(
            html.Td(all_stats[name + '_time_stat']['popular_day']))
        td_array.append(
            html.Td(all_stats[name + '_time_stat']['popular_hour']))

        usr_tr.append(html.Tr(children=td_array))
        td_array = []

        td_array.append(html.Td(name))
        td_array.append(
            html.Td(all_stats[name + '_station_stat']['popular_start_st']))
        td_array.append(
            html.Td(all_stats[name + '_station_stat']['popular_end_st']))
        td_array.append(
            html.Td(all_stats[name + '_station_stat']['popular_st']))
        td_array.append(
            html.Td(all_stats[name + '_trip_stat']['mean_trip_time']))
        td_array.append(
            html.Td(all_stats[name + '_trip_stat']['total_trip_time']))
        tr_array.append(html.Tr(children=td_array))
        td_array = []

    smthin = html.Table(children=[
        html.Thead(children=[
            html.Tr(children=[
                html.Th('City'),
                html.Th('Popular Start Station'),
                html.Th('Popular End Station'),
                html.Th('Popular Route (Start-End St. Combination)'),
                html.Th('Mean Trip Duration of all the Trips'),
                html.Th('Trip Duration of all the Trips'),
            ]),
        ]),
        html.Tbody(children=tr_array)
    ],
        style={
        'text-transform': 'capitalize'
    })

    other_thing = html.Table(children=[
        html.Thead(children=[
            html.Tr(children=[
                html.Th('City'),
                html.Th('Subscribers'),
                html.Th('Customers'),
                html.Th('Popular Month'),
                html.Th('Popular Day of the Week'),
                html.Th('Popular Hour of the Day'),
            ]),
        ]),
        html.Tbody(children=usr_tr)
    ],
        style={
        'text-transform': 'capitalize'
    })

    return [smthin, other_thing]
