python
import pandas as pd
import plotly.express as px

# Load the dataset
url = "https://opendata.abudhabi.ae/datasets/freelance-business-licenses"
dataset = pd.read_excel(url)

# Data preprocessing
# Fill NA values and filter necessary columns
dataset.fillna("Unknown", inplace=True)
filtered_df = dataset[['Trade Name (English)', 'License Type', 'Classification', 'Establishment Date']]

# Create an interactive bar chart using Plotly
fig = px.bar(
    filtered_df.groupby('License Type').size().reset_index(name='Counts'),
    x='License Type',
    y='Counts',
    title='Distribution of License Types',
    labels={'Counts': 'Number of Licenses', 'License Type': 'Type of License'}
)

# Show the dashboard chart
fig.show()
