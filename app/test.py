from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'Month': ['2024-01', '2024-02'],
    'Frequency': [3.2, 4.5],
    'team_id': ['team_01', 'team_01']
})

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='team-selector',
        options=[{'label': t, 'value': t} for t in df['team_id'].unique()],
        value=['team_01'],
        multi=True
    ),
    dcc.Graph(id='deployment-frequency-graph')
])

@app.callback(
    Output('deployment-frequency-graph', 'figure'),
    Input('team-selector', 'value')
)
def update_deployment_graph(selected_teams):
    print("✅ CALLBACK HIT")
    filtered_df = df[df['team_id'].isin(selected_teams)]
    return px.bar(filtered_df, x='Month', y='Frequency', color='team_id')

if __name__ == '__main__':
    app.run(debug=True)