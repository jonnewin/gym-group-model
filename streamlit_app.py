
import streamlit as st
import pandas as pd
from assumptions import ASSUMPTIONS
from revenue_model import build_revenue
from cost_model import build_operating_costs
from capex_model import build_capex
from pnl_model import build_pnl
from cashflow_model import build_cashflow
from balance_sheet import build_balance_sheet
from returns_model import calculate_returns

st.set_page_config(page_title="Gym Group LBO Model", layout="wide")

st.title("💪 Gym Group LBO Model")
st.markdown("Interactive LBO model simulation using operational assumptions.")

with st.sidebar:
    st.header("Model Assumptions")
    arpu = st.slider("ARPU (£)", 15, 40, ASSUMPTIONS["monthly_arpu"])
    churn = st.slider("Monthly Churn", 0.01, 0.10, ASSUMPTIONS["churn_rate"])
    avg_members = st.slider("Avg Members per Site", 1000, 3000, ASSUMPTIONS["avg_members"])
    exit_mult = st.slider("Exit EBITDA Multiple", 6.0, 15.0, ASSUMPTIONS["exit_ebitda_multiple"])
    equity = st.number_input("Initial Equity (£m)", value=ASSUMPTIONS["initial_equity"])
    debt = st.number_input("Initial Debt (£m)", value=ASSUMPTIONS["initial_debt"])

ASSUMPTIONS["monthly_arpu"] = arpu
ASSUMPTIONS["churn_rate"] = churn
ASSUMPTIONS["avg_members"] = avg_members
ASSUMPTIONS["exit_ebitda_multiple"] = exit_mult
ASSUMPTIONS["initial_equity"] = equity
ASSUMPTIONS["initial_debt"] = debt

# Initialize model
df = pd.DataFrame({
    "Month": pd.date_range(start=ASSUMPTIONS["start_date"], periods=ASSUMPTIONS["months"], freq='MS')
})
df["New Sites"] = ASSUMPTIONS["new_sites"]

# Build model pipeline
df = build_revenue(df, ASSUMPTIONS)
df = build_operating_costs(df, ASSUMPTIONS)
df = build_capex(df, ASSUMPTIONS)
df = build_pnl(df, ASSUMPTIONS)
df = build_cashflow(df, ASSUMPTIONS)
df = build_balance_sheet(df, ASSUMPTIONS)
results = calculate_returns(df, ASSUMPTIONS)

# Show results
st.subheader("📊 Model Outputs")
st.metric("Exit Value (£m)", f"{results['exit_value']:,.0f}")
st.metric("Equity Value (£m)", f"{results['equity_value']:,.0f}")
st.metric("MOIC", f"{results['moic']:.2f}")
st.metric("IRR", f"{results['irr']:.2%}")

with st.expander("📈 Full Model Data"):
    st.dataframe(df.style.format({"Revenue": "£{:,.2f}", "EBITDA": "£{:,.2f}"}))
