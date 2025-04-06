def build_pnl(df, assumptions):
    df["COGS"] = df["Revenue"] * assumptions["cogs_pct"]
    df["Gross Profit"] = df["Revenue"] - df["COGS"]
    df["EBITDA"] = df["Gross Profit"] - df["Opex"]
    return df
