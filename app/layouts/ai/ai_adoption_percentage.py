# adoption_by_team.py
from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_ai_adoption_percentage_by_team
from app.components.helpers import create_metric_card
from app.components.team_selector import team_selector_dropdown

# Load data for dropdown
df = get_ai_adoption_percentage_by_team()
print("ai adoption % DataFrame loaded in layout:", df.head())
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty and 'team_id' in df.columns else []
print("Team IDs for dropdown:", team_ids)
layout = html.Div([
    html.H1("AI Adoption % by Team", className="main-header mb-2"),
    html.P("Track AI adoption rates across teams", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Adoption %", "82", "+3", "🤖"), width=4),
        dbc.Col(create_metric_card("Teams Reporting", str(len(team_ids)), "", "👥"), width=4),
    ]),

    team_selector_dropdown('ai-adoption-percentage-team-selector', team_ids),

    dcc.Graph(id='ai-adoption-percentage-graph')
])


