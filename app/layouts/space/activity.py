from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from app.components.helpers import create_metric_card
from app.data.metrics_data import get_activity_trend_data
import pandas as pd
from app.components.team_selector import team_selector_dropdown

# Load data for dropdown
df = get_activity_trend_data()
print("Activity DataFrame loaded in layout:", df.head())
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty and 'team_id' in df.columns else []
print("Team IDs for dropdown:", team_ids)

layout = html.Div([
    html.H1("Activity", className="main-header mb-2"),
    html.P("Volume and frequency of developer actions", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("AI Prompts", "160", "+23%", "⚡"), width=4),
        dbc.Col(create_metric_card("Commits", "200", "+5%", "💾"), width=4),
    ]),

    team_selector_dropdown('activity-team-selector', team_ids),

    dcc.Graph(id='activity-graph')
])
