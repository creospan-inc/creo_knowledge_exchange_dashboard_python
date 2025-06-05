from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_failure_rate_data
from app.components.helpers import create_metric_card
from app.components.team_selector import team_selector_dropdown

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
    team_selector_dropdown('failure-rate-team-selector', team_ids),

    dcc.Graph(id='failure-rate-graph')
])
