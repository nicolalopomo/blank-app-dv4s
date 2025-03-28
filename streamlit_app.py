import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Set page title
st.set_page_config(page_title="Data Visualization App", layout="wide")

# Generate sample data
def generate_data(num_rows=100):
    np.random.seed(42)
    data = pd.DataFrame({
        'Category': np.random.choice(['A', 'B', 'C', 'D'], size=num_rows),
        'X': np.random.randn(num_rows) * 10 + 50,
        'Y': np.random.randn(num_rows) * 5 + 25,
        'Z': np.random.randint(1, 100, size=num_rows)
    })
    return data

# Load Data
df = generate_data(200)

# Sidebar options
st.sidebar.header("Settings")
num_rows = st.sidebar.slider("Number of Data Points", min_value=50, max_value=500, value=200, step=50)
df = generate_data(num_rows)

# Display raw data
if st.sidebar.checkbox("Show Raw Data", False):
    st.write("### Raw Data", df)

# Matplotlib Visualization
st.write("## Matplotlib Scatter Plot")
fig, ax = plt.subplots()
colors = {'A': 'red', 'B': 'blue', 'C': 'green', 'D': 'purple'}
ax.scatter(df["X"], df["Y"], c=df["Category"].map(colors), alpha=0.6)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_title("Matplotlib Scatter Plot")
st.pyplot(fig)

# Plotly Interactive Chart
st.write("## Plotly Interactive Scatter Plot")
fig = px.scatter(df, x="X", y="Y", color="Category", size="Z", title="Plotly Scatter Plot")
st.plotly_chart(fig, use_container_width=True)

# Bar Chart
st.write("## Bar Chart")
fig_bar = px.bar(df, x="Category", y="Z", color="Category", title="Bar Chart")
st.plotly_chart(fig_bar, use_container_width=True)

# End
st.sidebar.info("Adjust settings from the sidebar to see changes.")
