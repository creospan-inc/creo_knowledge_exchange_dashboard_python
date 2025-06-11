from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_satisfaction_data
import plotly.express as px
from app.components.helpers import create_metric_card
from app.components.team_selector import team_selector_dropdown

# Load data for dropdown
df = get_satisfaction_data()
# print("Satisfaction DataFrame loaded in layout:", df.head())
team_ids = sorted(df['team_id'].dropna().unique()) if not df.empty and 'team_id' in df.columns else []
# print("Team IDs for dropdown:", team_ids)

layout = html.Div([
    html.H1("Developer Satisfaction", className="main-header mb-2"),
    html.P("Satisfaction with AI tools and workflows", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current", "72%", "+3%", "😊"), width=4),
        dbc.Col(create_metric_card("Benchmark", "65%", "Industry Avg", "📊"), width=4),
    ]),

    team_selector_dropdown('satisfaction-team-selector', team_ids),

    dcc.Graph(id='satisfaction-graph')
])
