import pandas as pd
from assumptions import ASSUMPTIONS
from revenue_model import build_revenue
from cost_model import build_operating_costs
from capex_model import build_capex
from pnl_model import build_pnl
from cashflow_model import build_cashflow
from balance_sheet import build_balance_sheet
from returns_model import calculate_returns

def run_model():
    df = pd.DataFrame({
        "Month": pd.date_range(start=ASSUMPTIONS["start_date"], periods=ASSUMPTIONS["months"], freq='MS')
    })
    df["New Sites"] = ASSUMPTIONS["new_sites"]
    df = build_revenue(df, ASSUMPTIONS)
    df = build_operating_costs(df, ASSUMPTIONS)
    df = build_capex(df, ASSUMPTIONS)
    df = build_pnl(df, ASSUMPTIONS)
    df = build_cashflow(df, ASSUMPTIONS)
    df = build_balance_sheet(df, ASSUMPTIONS)
    results = calculate_returns(df, ASSUMPTIONS)
    print(df.head())
    print("Returns:", results)

if __name__ == "__main__":
    run_model()
