from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from app.data.metrics_data import get_failure_rate_data
from app.components.helpers import create_metric_card



layout = html.Div([
    html.H1("Change Failure Rate", className="main-header mb-2"),
    html.P("How often deployments fail", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current Failure Rate", "15%", "-25%", "⚠️"), width=4),
        dbc.Col(create_metric_card("Goal", "< 15%", "Target", "🎯"), width=4),
    ], className="mb-4"),

    dcc.Graph(
        figure=px.bar(get_failure_rate_data(), x='Month', y='Failure Rate', title="Failure Rate by Month")
    )
])
