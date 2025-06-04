from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_communication_data
import plotly.express as px
from app.components.helpers import create_metric_card

# Load data for dropdown
df = get_communication_data()
print("Communication DataFrame loaded in layout:", df.head())
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty and 'team_id' in df.columns else []
print("Team IDs for dropdown:", team_ids)

layout = html.Div([
    html.H1("Communication", className="main-header mb-2"),
    html.P("Collaboration and information sharing", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Collaboration", "80", "+5", "🤝"), width=4),
    ]),

    dcc.Dropdown(
        id='communication-team-selector',
        options=[{'label': team, 'value': team} for team in team_ids],
        value=team_ids,
        multi=True,
        placeholder="Select teams to display"
    ),

    dcc.Graph(id='communication-graph')
])
