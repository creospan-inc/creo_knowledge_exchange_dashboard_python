from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_efficiency_trend_data
import plotly.express as px
from app.components.helpers import create_metric_card
from app.components.team_selector import team_selector_dropdown

# Load data for dropdown

df = get_efficiency_trend_data()
print("Efficiency DataFrame loaded in layout:", df.head())
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty and 'team_id' in df.columns else []
print("Team IDs for dropdown:", team_ids)

layout = html.Div([
    html.H1("Efficiency", className="main-header mb-2"),
    html.P("Time saved and overhead reduction from AI", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Time Saved", "48 hrs", "+33%", "⏳"), width=4),
        dbc.Col(create_metric_card("Productive Hours", "34 hrs", "+9%", "💡"), width=4),
    ]),

    team_selector_dropdown('efficiency-team-selector', team_ids),

    dcc.Graph(id='efficiency-graph')
])