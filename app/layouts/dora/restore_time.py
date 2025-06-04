from dash import html, dcc
import dash_bootstrap_components as dbc
from app.components.helpers import create_metric_card
from app.data.metrics_data import get_restore_time_data

# Load data once to populate dropdown safely
df = get_restore_time_data()
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty else []

layout = html.Div([
    html.H1("Time to Restore Service", className="main-header mb-2"),
    html.P("How quickly services are restored after failure", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current MTTR", "4.2 hours", "-35%", "🛠️"), width=4),
        dbc.Col(create_metric_card("Goal", "< 1 hour", "Target", "🎯"), width=4),
    ], className="mb-4"),

    # Dropdown to select teams
    dcc.Dropdown(
        id='restore-time-team-selector',
        options=[{'label': team, 'value': team} for team in team_ids],
        value=team_ids,
        multi=True,
        placeholder="Select teams to display"
    ),

    dcc.Graph(id='restore-time-graph')
])
