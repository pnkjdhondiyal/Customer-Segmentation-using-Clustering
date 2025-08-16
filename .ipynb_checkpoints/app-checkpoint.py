import streamlit as st
import pandas as pd
from src.clustering import perform_clustering
from src.visualization import plot_3d_clusters

st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

st.title("🛍 Customer Segmentation using K-Means")

# Upload dataset
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview", df.head())

    # Feature selection
    features = st.multiselect(
        "Select features for clustering:",
        options=df.columns.tolist(),
        default=["Age", "Annual Income (k$)", "Spending Score (1-100)"]
    )

    n_clusters = st.slider("Number of clusters", 2, 10, 5)

    if st.button("Run Clustering"):
        df, model = perform_clustering(df, features, n_clusters)
        st.write("### Clustered Data", df.head())

        fig = plot_3d_clusters(df)
        st.plotly_chart(fig, use_container_width=True)
