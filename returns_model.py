def calculate_returns(df, assumptions):
    exit_ebitda = df["EBITDA"].iloc[-1] * 12
    exit_value = exit_ebitda * assumptions["exit_ebitda_multiple"]
    equity_value = exit_value - assumptions["initial_debt"]
    moic = equity_value / assumptions["initial_equity"]
    irr = (moic ** (1 / 5)) - 1
    return {"exit_value": exit_value, "equity_value": equity_value, "moic": moic, "irr": irr}
