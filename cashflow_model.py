def build_cashflow(df, assumptions):
    df["WC"] = df["Revenue"] * 0.02
    df["Interest"] = assumptions["initial_debt"] * assumptions["interest_rate"] / 12
    df["FCF"] = df["EBITDA"] - df["Total CapEx"] - df["WC"] - df["Interest"]
    return df
