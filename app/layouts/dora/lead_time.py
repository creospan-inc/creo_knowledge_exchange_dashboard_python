from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_lead_time_data
from app.components.helpers import create_metric_card
from app.components.team_selector import team_selector_dropdown

# Load data once to populate dropdown safely
df = get_lead_time_data()
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty else []

layout = html.Div([
    html.H1("Lead Time for Changes", className="main-header mb-2"),
    html.P("Time from commit to production", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current Lead Time", "4.2 days", "-6%", "⏱️"), width=4),
        dbc.Col(create_metric_card("Target", "< 1 day", "Goal", "🎯"), width=4),
    ], className="mb-4"),

    # Dropdown to select teams
        team_selector_dropdown('lead-time-team-selector', team_ids),

    dcc.Graph(id='lead-time-graph')
])
