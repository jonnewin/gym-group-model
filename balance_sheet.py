def build_balance_sheet(df, assumptions):
    df["Cash"] = df["FCF"].cumsum()
    df["Debt"] = assumptions["initial_debt"]
    df["Equity"] = assumptions["initial_equity"]
    df["Net Assets"] = df["Cash"] + df["Equity"] - df["Debt"]
    return df
