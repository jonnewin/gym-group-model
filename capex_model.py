def build_capex(df, assumptions):
    df["Expansion CapEx"] = df["New Sites"] * assumptions["capex_per_new_site"] / 1e6
    df["Maintenance CapEx"] = df["Total Sites"] * assumptions["maint_capex_per_site"] / 1e6
    df["Total CapEx"] = df["Expansion CapEx"] + df["Maintenance CapEx"]
    return df
