from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_failure_rate_data
from app.components.helpers import create_metric_card

# Load data once to populate dropdown safely
# Assumes your failure_rate_data table has a 'team_id' column

df = get_failure_rate_data()
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty else []

layout = html.Div([
    html.H1("Change Failure Rate", className="main-header mb-2"),
    html.P("How often deployments fail", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current Failure Rate", "15%", "-25%", "⚠️"), width=4),
        dbc.Col(create_metric_card("Goal", "< 15%", "Target", "🎯"), width=4),
    ], className="mb-4"),

    # Dropdown to select teams
    dcc.Dropdown(
        id='failure-rate-team-selector',
        options=[{'label': team, 'value': team} for team in team_ids],
        value=team_ids,
        multi=True,
        placeholder="Select teams to display"
    ),

    dcc.Graph(id='failure-rate-graph')
])
