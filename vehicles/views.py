import pandas as pd
from django.shortcuts import render
from .dashboard import (
    frequency_table,
    expensive_vehicles_table,
    groupby_table,
)


def dashboard_view(request):
    queryset = pd.read_csv("dummy_data/vehicles_data_1000.csv")
    df = pd.DataFrame(queryset)

    # Ensure compatibility whether dataset has 'selling_price' or 'price'
    if 'selling_price' not in df.columns and 'price' in df.columns:
        df['selling_price'] = df['price']
    elif 'price' not in df.columns and 'selling_price' in df.columns:
        df['price'] = df['selling_price']

    return render(request, "vehicles/index.html", {
        "frequency_table": frequency_table(df),
        "expensive_vehicles_table": expensive_vehicles_table(df, min_price=5000),
        "groupby_table": groupby_table(df),
    })
