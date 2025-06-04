from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_sprint_burndown_data
from app.components.helpers import create_metric_card

# Load data once to populate dropdown safely
df = get_sprint_burndown_data()
print("Sprint Burndown DataFrame loaded in layout:", df.head())
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty else []
print("Team IDs for dropdown:", team_ids)

layout = html.Div([
    html.H1("Sprint Burndown", className="main-header mb-2"),
    html.P("Track remaining work throughout the sprint", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current Sprint", "Sprint 26", "", "📉"), width=4),
    ]),

    # Dropdown to select teams
    dcc.Dropdown(
        id='sprint-burndown-team-selector',
        options=[{'label': team, 'value': team} for team in team_ids],
        value=team_ids,
        multi=True,
        placeholder="Select teams to display"
    ),

    dcc.Graph(id='sprint-burndown-graph')
])
