import pandas as pd
import requests
from dash import Dash, dash_table, dcc, html

app = Dash(__name__)

# API endpoint for the Tree Inventory dataset
url = "https://data.winnipeg.ca/resource/hfwk-jp4h.json"
response = requests.get(url)
data = response.json()

# Check if the response contains an error
if isinstance(data, dict) and 'error' in data:
    print("API Error:", data['error'])
else:
    df = pd.DataFrame(data)

    # Print the DataFrame to understand its structure
    print(df)

    # Preprocess the DataFrame to convert complex data types to strings
    if 'location' in df.columns:
        df['location'] = df['location'].astype(str)
    if 'point' in df.columns:
        df['point'] = df['point'].astype(str)

    app.layout = html.Div([
        html.H1("City of Winnipeg Tree Inventory"),

        # Dash DataTable
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            page_size=10  # Display 10 rows per page for better readability
        ),

        # Dash Graph
        dcc.Graph(
            id='graph',
            figure={
                'data': [
                    # Scatter plot of Botanical Name vs Diameter at Breast Height
                    {'x': df['botanical_name'], 'y': df['diameter_at_breast_height'], 'type': 'scatter', 'mode': 'markers', 'name': 'Botanical Name vs Diameter'},
                ],
                'layout': {
                    'title': 'Tree Inventory - Botanical Name vs Diameter at Breast Height',
                    'xaxis': {'title': 'Botanical Name'},
                    'yaxis': {'title': 'Diameter at Breast Height (inches)'},
                }
            }
        )
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)
