from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_velocity_data
import plotly.express as px
from app.components.helpers import create_metric_card

# Load data once to populate dropdown safely
df = get_velocity_data()
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty else []

layout = html.Div([
    html.H1("Velocity", className="main-header mb-2"),
    html.P("Completed work per sprint", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current Velocity", "36 pts", "+12%", "🚀"), width=4),
    ]),

    # Dropdown to select teams
    dcc.Dropdown(
        id='velocity-team-selector',
        options=[{'label': team, 'value': team} for team in team_ids],
        value=team_ids,
        multi=True,
        placeholder="Select teams to display"
    ),

    dcc.Graph(id='velocity-graph')
])
