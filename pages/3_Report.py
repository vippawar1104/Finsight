import streamlit as st
import pandas as pd
import plotly.express as px
import os
from dotenv import load_dotenv
from src.utils.expense_tracker import Account
from src.utils.finbot import get_budget_insights
from src.config import get_user_db_path


load_dotenv()

# Guarded Cohere import + availability flag to prevent ModuleNotFoundError
try:
    import cohere  # type: ignore
    api_key = os.getenv('COHERE_API_KEY')
    COHERE_AVAILABLE = bool(api_key)
except ModuleNotFoundError:
    COHERE_AVAILABLE = False



if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in first.")
    st.stop()

user_email = st.session_state.user_email
db_name = str(get_user_db_path(user_email))
account = Account(db_name=db_name)

st.title("📊 Financial Reports")
st.write("A finance report of your cash.")
st.divider()
# Fetch Expenses & Income
expenses_df = account.expenseList()
income_df = account.incomeList()


if not expenses_df.empty:
    expenses_df['date'] = pd.to_datetime(expenses_df['date'])
if not income_df.empty:
    income_df['date'] = pd.to_datetime(income_df['date'])

col1, col2 = st.columns(2)
with col1:
    if not expenses_df.empty:
      
        if not expenses_df.empty:
            category_data = expenses_df.groupby("category")["amount"].sum().reset_index()
            fig_expense_pie = px.pie(
                category_data,
                values="amount",
                names="category",
                title="Expenses by Category",
                hole=0.4
            )
            st.plotly_chart(fig_expense_pie)
        else:
            st.write("No expenses recorded yet.")

# Income Breakdown
with col2:
    if not income_df.empty:

      
        if not income_df.empty:
            income_data = income_df.groupby("source")["amount"].sum().reset_index()
            fig_income_pie = px.pie(
                income_data,
                values="amount",
                names="source",
                title="Income Breakdown by Category",
                hole=0.4
            )
            st.plotly_chart(fig_income_pie)
# Add month column to dataframes if they have data
if not expenses_df.empty:
    expenses_df["month"] = expenses_df["date"].dt.strftime("%Y-%m")

if not income_df.empty:
    income_df["month"] = income_df["date"].dt.strftime("%Y-%m")

# Monthly Expense vs Income Trend
if not expenses_df.empty and not income_df.empty:
    monthly_expense = expenses_df.groupby("month")["amount"].sum().reset_index()
    monthly_income = income_df.groupby("month")["amount"].sum().reset_index()

    # Create an area chart (stacked)
    fig = px.area(
        pd.concat([monthly_expense.assign(Type="Expense"), monthly_income.assign(Type="Income")]),
        x="month",
        y="amount",
        color="Type",
        title="Monthly Expense vs Income Trend",
        line_group="Type", 
        markers=True
    )
    st.plotly_chart(fig)


# Bar Chart: Monthly Spending by Category
if not expenses_df.empty:
    category_monthly_data = expenses_df.groupby(["month", "category"])["amount"].sum().reset_index()
    fig_category_bar = px.bar(category_monthly_data, x="month", y="amount", color="category", barmode="group", title="Monthly Spending by Category")
    st.plotly_chart(fig_category_bar)



# Stacked Bar Chart: Income vs Expenses

if not expenses_df.empty and not income_df.empty:
  
    stacked_data = pd.concat([
        monthly_expense.assign(Type="Expense"),
        monthly_income.assign(Type="Income")
    ])
    fig_stacked_bar = px.bar(stacked_data, x="month", y="amount", color="Type", barmode="stack", title="Stacked Income vs Expenses")
    st.plotly_chart(fig_stacked_bar)




#SYNBOT
with st.sidebar:
    st.markdown(
        """
        <style>
        .chatbot-container {
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            margin-bottom: 20px;
        }

        .chatbot-icon {
            background-color: #ff4b87;
            color: white;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            font-size: 20px;
            font-weight: bold;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
        }

        .chatbot-name {
            background-color: white;
            color: #333;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: bold;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        }
        </style>
        <div class="chatbot-container" onclick="document.getElementById('chat_expander').click();">
            <div class="chatbot-icon">🤖</div>
            <div class="chatbot-name">FinBot - AI Assistant</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Expander for AI Chat (appears when button is clicked)
    with st.expander("💬 Chat with FinBot", expanded=False):
        st.write(f"👋 Hi {st.session_state.user_email.split('@')[0]}! How can I help you today")

        user_query = st.text_input("Enter your question:")

        if st.button("Send ▶"):
            if user_query.strip():
                transactions_text = account.format_transactions_for_ai()
                budget_tip = get_budget_insights(user_query, transactions_text)
                st.write(budget_tip)
            else: 
                st.warning("Please enter a valid question.")
