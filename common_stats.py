import dash_core_components as dcc
import dash_html_components as html
import bikeshare_2 as bs


def other_stats():
    all_df = {}
    all_df['chicago_df'] = bs.load_data('chicago','all','all')
    all_df['new_york'] = bs.load_data('new york city','all','all')
    all_df['washington'] = bs.load_data('washington','all','all')

    all_stats = {}
    for name, df in zip(all_df.keys(), all_df.values()):

        all_stats[name + '_station_stat'] = bs.station_stats(df)
        all_stats[name + '_trip_stat'] = bs.trip_duration_stats(df)

    print(all_stats.keys())
    # smthin = [
    #     html.P(children=[
    #         html.Span(
    #             'Popluar start station of the city is '
    #         ),
    #         html.Span(
    #             children=[station_stat['popular_start_st']],
    #             style={
    #                 'text-transform': 'capitalize',
    #                 'font-weight': 'bold'
    #             }
    #         ),
    #     ]),
    #     html.P(children=[
    #         html.Span(
    #             'Popluar end station of the city is '
    #         ),
    #         html.Span(
    #             children=[station_stat['popular_end_st']],
    #             style={
    #                 'text-transform': 'capitalize',
    #                 'font-weight': 'bold'
    #             }
    #         ),
    #     ]),
    #     html.P(children=[
    #         html.Span(
    #             'Popular route i.e. Start and End station combination people use the most is '
    #         ),
    #         html.Span(
    #             children=[station_stat['popular_st']],
    #             style={
    #                 'text-transform': 'capitalize',
    #                 'font-weight': 'bold'
    #             }
    #         ),
    #     ]),
    #     html.P(children=[
    #         html.Span(
    #             'Mean trip duration time of all the trips: '
    #         ),
    #         html.Span(
    #             children=[trip_stat['mean_trip_time']],
    #             style={
    #                 'text-transform': 'capitalize',
    #                 'font-weight': 'bold'
    #             }
    #         ),
    #     ]),
    #     html.P(children=[
    #         html.Span(
    #             'Total trip duration time of all the trips: '
    #         ),
    #         html.Span(
    #             children=[trip_stat['total_trip_time']],
    #             style={
    #                 'text-transform': 'capitalize',
    #                 'font-weight': 'bold'
    #             }
    #         ),
    #     ]),
    # ]

    # return smthin
