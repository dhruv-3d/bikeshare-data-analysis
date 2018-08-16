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

    return all_stats.keys()

print(other_stats())
