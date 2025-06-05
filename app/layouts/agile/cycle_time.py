from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_cycle_time_data
import plotly.express as px
from app.components.helpers import create_metric_card
from app.components.team_selector import team_selector_dropdown

# Load data once to populate dropdown safely
df = get_cycle_time_data()
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty else []

layout = html.Div([
    html.H1("Cycle Time", className="main-header mb-2"),
    html.P("Time from start to finish for tasks", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current", "5.2 days", "-20%", "⏱️"), width=4),
    ]),

    # Dropdown to select teams
    team_selector_dropdown('cycle-time-team-selector', team_ids),

    dcc.Graph(id='cycle-time-graph')
])
