import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="AI Budgeter", layout="wide")
st.title("💰 Universal Finance Predictor")

def get_prediction(df):
    try:
        df_copy = df.copy()
        df_copy['Date'] = pd.to_datetime(df_copy['Date'])
        df_copy = df_copy.sort_values('Date')
        
        # Group by month
        monthly = df_copy.groupby(df_copy['Date'].dt.to_period('M'))['Amount'].sum().reset_index()
        
        if len(monthly) < 2:
            return None, monthly['Amount'].iloc[0] if not monthly.empty else 0

        # Linear Regression
        monthly['MonthNum'] = np.arange(len(monthly))
        X = monthly[['MonthNum']]
        y = monthly['Amount']
        
        model = LinearRegression()
        model.fit(X, y)
        
        next_month = np.array([[monthly['MonthNum'].max() + 1]])
        pred = model.predict(next_month)[0]
        return round(float(max(0, pred)), 2), None
    except Exception as e:
        return f"Error: {e}", None

uploaded_files = st.file_uploader(
    "Upload your transaction CSVs (You can select multiple files at once)", 
    type="csv", 
    accept_multiple_files=True
)

if uploaded_files:
    all_dataframes = []
    for file in uploaded_files:
        df_temp = pd.read_csv(file)
        all_dataframes.append(df_temp)
    
    df = pd.concat(all_dataframes, ignore_index=True)
    
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Monthly Spending Trend")
        monthly_plot = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum()
        monthly_plot.index = monthly_plot.index.astype(str)
        st.bar_chart(monthly_plot)

    with col2:
        st.subheader("Spending by Category")
        cat_plot = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
        st.bar_chart(cat_plot)

    st.divider()
    prediction, current_total = get_prediction(df)

    st.subheader("🔮 AI Spending Forecast")
    if isinstance(prediction, float):
        st.success(f"Based on your history, next month's estimated total is: **${prediction:,.2f}**")
        
        last_month_actual = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum().iloc[-1]
        diff = prediction - last_month_actual
        if diff > 0:
            st.warning(f"Trend Alert: Spending is projected to increase by **${diff:,.2f}** compared to last month.")
        else:
            st.info(f"Good news: Spending is projected to decrease by **${abs(diff):,.2f}**.")
    else:
        st.info(f"Total spending so far: **${current_total:,.2f}**. Upload more months of data to see a trend prediction!")

    with st.expander("Show Combined Transaction List"):
        display_df = df.copy()
        display_df['Date'] = display_df['Date'].dt.strftime('%Y-%m-%d')
        st.dataframe(display_df, use_container_width=True)

else:

    st.info("Please upload one or more CSV files to begin.")
