def build_operating_costs(df, assumptions):
    df["Rent"] = df["Total Sites"] * assumptions["rent_per_site"] / 1e6
    df["Staff"] = df["Total Sites"] * assumptions["staff_per_site"] / 1e6
    df["Utilities"] = df["Total Sites"] * assumptions["utilities_per_site"] / 1e6
    df["Tech"] = df["Total Sites"] * assumptions["tech_per_site"] / 1e6
    df["Opex"] = df[["Rent", "Staff", "Utilities", "Tech"]].sum(axis=1)
    return df
