from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from app.data.metrics_data import get_lead_time_data
from app.components.helpers import create_metric_card


layout = html.Div([
    html.H1("Lead Time for Changes", className="main-header mb-2"),
    html.P("Time from commit to production", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current Lead Time", "4.2 days", "-6%", "⏱️"), width=4),
        dbc.Col(create_metric_card("Target", "< 1 day", "Goal", "🎯"), width=4),
    ], className="mb-4"),

    dcc.Graph(
        figure=px.line(get_lead_time_data(), x='Month', y='Lead Time', title="Lead Time Over Time")
    )
])
