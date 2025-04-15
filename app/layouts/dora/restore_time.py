from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from app.components.helpers import create_metric_card
from app.data.metrics_data import get_restore_time_data

layout = html.Div([
    html.H1("Time to Restore Service", className="main-header mb-2"),
    html.P("How quickly services are restored after failure", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current MTTR", "4.2 hours", "-35%", "🛠️"), width=4),
        dbc.Col(create_metric_card("Goal", "< 1 hour", "Target", "🎯"), width=4),
    ], className="mb-4"),

    dcc.Graph(
        figure=px.line(get_restore_time_data(), x='Month', y='Restore Time', title="Time to Restore Service")
    )
])
