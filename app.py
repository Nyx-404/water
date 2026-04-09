import streamlit as st
import pandas as pd

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Rainwater Harvesting DSS", layout="centered")

st.title("💧 Rainwater Harvesting Decision Support System")
st.subheader("Prediction and Recommendation Module")

# -------------------------------
# USER INPUT
# -------------------------------
st.header("🔹 Enter Input Parameters")

rainfall = st.number_input("Monthly Rainfall (mm)", min_value=0.0, value=100.0)
area = st.number_input("Catchment Area (m²)", min_value=0.0, value=100.0)
runoff = st.number_input("Runoff Coefficient", min_value=0.0, max_value=1.0, value=0.8)
demand = st.number_input("Monthly Water Demand (L)", min_value=0.0, value=2500.0)
tank = st.number_input("Tank Capacity (L)", min_value=0.0, value=10000.0)

# -------------------------------
# CALCULATION
# -------------------------------

if st.button("Predict"):

    harvested = rainfall * area * runoff
    net_water = harvested - demand

    months_list = []
    storage = 0

    # simulate for 12 months
    for i in range(1, 13):
        storage = storage + harvested - demand

        if storage < 0:
            storage = 0
            status = "Shortage"
        elif storage > tank:
            storage = tank
            status = "Overflow"
        else:
            status = "Sufficient"

        months_list.append({
            "Month": i,
            "Storage": storage,
            "Status": status
        })

    df = pd.DataFrame(months_list)

    harvested = rainfall * area * runoff
    net_water = harvested - demand

    # Estimate months water lasts
    if demand > 0:
        months = harvested / demand
    else:
        months = 0

    # Storage check
    if net_water <= 0:
        status = "Shortage ❌"
    elif net_water >= tank:
        status = "Overflow ⚠️"
    else:
        status = "Sufficient ✅"

    # Sustainability
    if months < 1:
        sustainability = "Low"
    elif months < 3:
        sustainability = "Moderate"
    else:
        sustainability = "High"

    # -------------------------------
    # OUTPUT
    # -------------------------------
    st.header("📊 Results")

    st.write(f"**Harvested Water:** {harvested:.2f} L")
    st.write(f"**Net Water:** {net_water:.2f} L")
    st.write(f"**Water lasts for:** {months:.2f} months")
    st.write(f"**Status:** {status}")
    st.write(f"**Sustainability Level:** {sustainability}")

    # Recommendation
    st.header("💡 Recommendation")

    if status == "Shortage ❌":
        st.warning("Increase catchment area or reduce water usage.")
    elif status == "Overflow ⚠️":
        st.warning("Increase tank capacity to store excess water.")
    else:
        st.success("System is working efficiently.")

    st.subheader("📈 Storage Trend Over Time")
    st.line_chart(df.set_index("Month")["Storage"])

    st.subheader("📋 Monthly Details")
    st.dataframe(df)

    st.header("💡 Recommendation")

    shortage_count = (df["Status"] == "Shortage").sum()
    overflow_count = (df["Status"] == "Overflow").sum()

    if shortage_count > 3:
        st.warning("System faces frequent shortages. Increase catchment area or reduce demand.")
    elif overflow_count > 3:
        st.warning("Frequent overflow detected. Increase tank capacity.")
    else:
        st.success("System is balanced and sustainable.")