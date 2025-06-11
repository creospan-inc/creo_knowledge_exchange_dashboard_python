# print(">>> deployment_frequency.py is being imported!")  # TOP-LEVEL DEBUG

from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from app import app
from app.data.metrics_data import get_deployment_frequency_data
from app.components.helpers import create_metric_card
from app.components.team_selector import team_selector_dropdown
# This file's callback only registers if the whole module is imported
# Make sure app_routes.py or main.py has: import app.layouts.dora.deployment_frequency

# Load data once to populate dropdown safely
df = get_deployment_frequency_data()
# print(">>> Initial DataFrame loaded in deployment_frequency.py:\n", df.head())
# print(">>> Columns:", df.columns)
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty else []
# print(">>> Team IDs for dropdown:", team_ids)

layout = html.Div([
    html.H1("Deployment Frequency", className="main-header mb-2"),
    html.P("How often each team deploys to production", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current Frequency", "3.1/week", "+10%", "🚀"), width=4),
        dbc.Col(create_metric_card("Goal", "4.0/week", "Target", "🎯"), width=4),
    ], className="mb-4"),

    # Dropdown to select teams
       team_selector_dropdown('team-selector', team_ids),

    dcc.Graph(id='deployment-frequency-graph')
])