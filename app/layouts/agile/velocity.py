from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_velocity_data
import plotly.express as px
from app.components.helpers import create_metric_card
from app.components.team_selector import team_selector_dropdown

# Load data once to populate dropdown safely
df = get_velocity_data()
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty else []

layout = html.Div([
    html.H1("Velocity", className="main-header mb-2"),
    html.P("Completed work per sprint", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current Velocity", "36 pts", "+12%", "🚀"), width=4),
    ]),

    
     team_selector_dropdown('velocity-team-selector', team_ids),

    dcc.Graph(id='velocity-graph')
])
