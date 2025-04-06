import pandas as pd

def build_revenue(df, assumptions):
    df["Total Sites"] = assumptions["starting_sites"] + df["New Sites"].cumsum()
    df["Revenue"] = df["Total Sites"] * assumptions["avg_members"] * assumptions["monthly_arpu"] / 1e6
    return df
