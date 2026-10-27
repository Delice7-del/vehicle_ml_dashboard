import plotly.express as px
import plotly.offline as opy
import plotly.graph_objects as go
import pandas as pd


def frequency_table(df):
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']

    table_html = manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )
    return table_html


def expensive_vehicles_table(df, min_price=5000):
    subset = df[df['selling_price'] > min_price]
    return subset.to_html(
        classes="table table-bordered table-striped table-sm",
        index=False,
        justify='center'
    )


def groupby_table(df):
    grouped = df.groupby(['manufacturer', 'transmission'])['selling_price'].mean().round(2).reset_index()
    return grouped.to_html(
        classes="table table-bordered table-striped table-sm",
        index=False,
        justify='center'
    )


grouped_vehicles_table = groupby_table
