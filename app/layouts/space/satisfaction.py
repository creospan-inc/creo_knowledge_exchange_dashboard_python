from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_satisfaction_data
import plotly.express as px
from app.components.helpers import create_metric_card


layout = html.Div([
    html.H1("Developer Satisfaction", className="main-header mb-2"),
    html.P("Satisfaction with AI tools and workflows", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current", "72%", "+3%", "😊"), width=4),
        dbc.Col(create_metric_card("Benchmark", "65%", "Industry Avg", "📊"), width=4),
    ]),

    dcc.Graph(
        figure=px.line(get_satisfaction_data(), x='Month', y='Score', title="Satisfaction Over Time")
    )
])
