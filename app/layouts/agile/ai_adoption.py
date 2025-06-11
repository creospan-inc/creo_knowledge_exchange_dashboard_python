from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_ai_adoption_data, get_ai_adoption_percentage_by_team
import plotly.express as px
from app.components.helpers import create_metric_card


layout = html.Div([
    html.H1("AI Adoption ", className="main-header mb-2"),
    html.P("How widely AI tools are being used in sprints", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current Rate", "68%", "+13%", "🤖"), width=4),
    ]),

    dcc.Graph(
        figure=px.line(get_ai_adoption_percentage_by_team(), x='Month', y='Adoption_Rate', title="AI Adoption Over Time")
    )
])
