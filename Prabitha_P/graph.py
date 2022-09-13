import pandas as pd
cars_data=pd.read_csv('cars_dataset.csv')
import plotly.express as px
fig = px.scatter(
    data_frame=cars_data[cars_data['kms_driven']>5000], 
    x='kms_driven', 
    y='Price', 
    size="kms_driven", 
    color="Price",
    hover_name="company",
    size_max=50
)
fig.write_html('graph.html')
