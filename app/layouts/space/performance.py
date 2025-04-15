from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_performance_data
import plotly.express as px
from app.components.helpers import create_metric_card


layout = html.Div([
    html.H1("Performance", className="main-header mb-2"),
    html.P("Quality and business impact of delivered work", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Quality", "80%", "+5%", "✅"), width=4),
        dbc.Col(create_metric_card("Impact", "70%", "+5%", "💥"), width=4),
    ]),

    dcc.Graph(
        figure=px.line(get_performance_data(), x='Month', y=['Quality', 'Impact'], title="Performance Over Time")
    )
])
