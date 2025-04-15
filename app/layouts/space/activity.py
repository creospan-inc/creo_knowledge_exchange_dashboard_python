from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from app.components.helpers import create_metric_card
from app.data.metrics_data import get_activity_trend_data

layout = html.Div([
    html.H1("Activity", className="main-header mb-2"),
    html.P("Volume and frequency of developer actions", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("AI Prompts", "160", "+23%", "⚡"), width=4),
        dbc.Col(create_metric_card("Commits", "200", "+5%", "💾"), width=4),
    ]),

    dcc.Graph(
        figure=px.line(get_activity_trend_data(), x='Month', y=['Prompts', 'Commits'], title="Developer Activity Trends")
    )
])
