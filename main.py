import pathlib
import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py


def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")


css_path = pathlib.Path(
    "./style.css")
load_css(css_path)

# Title
st.markdown(f"""
    <div class='title'>
    <div class="heading">
    Lauki Finance: Credit Risk Modelling
    </div>
    </div>
    """, unsafe_allow_html=True)

# Create rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the first row with default values
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('Income', min_value=0, value=1200000)
with row1[2]:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)

# Calculate Loan to Income Ratio and display it
loan_to_income_ratio = loan_amount / income if income > 0 else 0

with row2[0]:
    st.markdown(f"""
    <div>
        <div class="loan_style">
            Loan to Income Ratio:
        </div>
        <div class="loan_value">
            {loan_to_income_ratio:.2f}
        </div>
    </div>
""", unsafe_allow_html=True)
    # st.text("Loan to Income Ratio:")
    # st.text(f"{loan_to_income_ratio:.2f}")  # Display as a text field

# Assign inputs to the remaining controls
with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)
with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

if st.button('Calculate Risk', key="calculate", help="Click to calculate risk"):
    # Call the predict function
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months,
        avg_dpd_per_delinquency, delinquency_ratio,
        credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    # Display the results
    # st.write(f"Default Probability: {probability:.2%}")
    # st.write(f"Credit Score: {credit_score}")
    # st.write(f"Rating: {rating}")
    # row1 = st.columns(3)
    # row2 = st.columns(3)
    # with row1[0]:
    #     st.write("Default Probability", key="Defualt_Probability")
    # with row1[1]:
    #     st.write("Credit Score")
    # with row1[2]:
    #     st.write("Rating")
    # with row2[0]:
    #     st.write(f"{probability:.2%}")
    # with row2[1]:
    #     st.write(f"{credit_score}")
    # with row2[2]:
    #     st.write(f"{rating}")
    # col1,col2,col3 = st.columns(3)
    # col1.metric("Default Probability",f"{probability:.2%}",key = "Probability")
    if probability >= 0.60:
        metric_value = "red-font"
    elif 0.40 <= probability < 0.60:
        metric_value = "yellow-font"
    else:
        metric_value = "green-font"

    if rating == "Poor":
        metric_container_rating = "red_container"
    elif rating == "Average":
        metric_container_rating = "yellow_container"
    else:
        metric_container_rating = "green_container"
    st.markdown(f"""
    <div class="metrics-row">
        <div class="metric-container">
            <div class="metric-label">Default Probability</div>
            <div class="{metric_value}">{probability:.2%}</div>
        </div>
        <div class="metric-container">
            <div class="metric-label">Credit Score</div>
            <div class="{metric_value}">{credit_score}</div>
        </div>
        <div class="{metric_container_rating}">
            <div class="metric_label_rating">Rating</div>
            <div class={metric_value}">{rating}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="info">This Project Created And Published By Mohamed Anees</div>
""", unsafe_allow_html=True
        )