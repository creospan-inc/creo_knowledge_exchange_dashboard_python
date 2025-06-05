from dash import html, dcc
import dash_bootstrap_components as dbc
from app.components.helpers import create_metric_card
from app.data.metrics_data import get_restore_time_data
from app.components.team_selector import team_selector_dropdown

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
    team_selector_dropdown('restore-time-team-selector', team_ids),

    dcc.Graph(id='restore-time-graph')
])
