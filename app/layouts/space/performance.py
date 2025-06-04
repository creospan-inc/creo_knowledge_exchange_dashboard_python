from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_performance_data
import plotly.express as px
from app.components.helpers import create_metric_card

# Load data for dropdown
df = get_performance_data()
print("Performance DataFrame loaded in layout:", df.head())
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty and 'team_id' in df.columns else []
print("Team IDs for dropdown:", team_ids)

layout = html.Div([
    html.H1("Performance", className="main-header mb-2"),
    html.P("Quality and impact of delivered work", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Quality", "80", "+5", "🏆"), width=4),
        dbc.Col(create_metric_card("Impact", "70", "+10", "🚀"), width=4),
    ]),

    dcc.Dropdown(
        id='performance-team-selector',
        options=[{'label': team, 'value': team} for team in team_ids],
        value=team_ids,
        multi=True,
        placeholder="Select teams to display"
    ),

    dcc.Graph(id='performance-graph')
])
