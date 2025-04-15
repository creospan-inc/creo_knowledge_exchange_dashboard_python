from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from app.data.metrics_data import get_deployment_frequency_data
from app.components.helpers import create_metric_card


layout = html.Div([
    html.H1("Deployment Frequency", className="main-header mb-2"),
    html.P("How often your team deploys to production", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current Frequency", "3.1/week", "+10%", "🚀"), width=4),
        dbc.Col(create_metric_card("Goal", "4.0/week", "Target", "🎯"), width=4),
    ], className="mb-4"),

    dcc.Graph(
        figure=px.bar(get_deployment_frequency_data(), x='Month', y='Frequency', title="Deployments per Month")
    )
])
