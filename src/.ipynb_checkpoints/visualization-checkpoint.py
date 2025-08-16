import plotly.express as px

def plot_3d_clusters(df):
    fig = px.scatter_3d(
        df, x='Age', y='Annual Income (k$)', z='Spending Score (1-100)',
        color='Cluster', symbol='Cluster', size_max=10, opacity=0.7
    )
    return fig
