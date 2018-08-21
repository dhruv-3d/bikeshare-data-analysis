import dash_core_components as dcc
import bikeshare_2 as bs

def month_selector(slider_id):

    range_makrs = {}

    for m in bs.MONTHS:
        range_makrs[bs.MONTHS.index(m) + 1] = m

    slider = dcc.RangeSlider(
        id=slider_id,
        min=1,
        max=6,
        step=None,
        marks=range_makrs,
        value=[1, 6],
    )

    return slider