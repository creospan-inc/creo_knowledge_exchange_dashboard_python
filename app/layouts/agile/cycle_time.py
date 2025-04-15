from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import cycle_time_data
import plotly.express as px
from app.components.helpers import create_metric_card


layout = html.Div([
    html.H1("Cycle Time", className="main-header mb-2"),
    html.P("Time from start to finish for tasks", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current", "5.2 days", "-20%", "⏱️"), width=4),
    ]),

    dcc.Graph(
        figure=px.line(cycle_time_data, x='Month', y='Cycle Time', title="Cycle Time Trend")
    )
])
