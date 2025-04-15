from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import get_communication_data
import plotly.express as px
from app.components.helpers import create_metric_card


layout = html.Div([
    html.H1("Communication", className="main-header mb-2"),
    html.P("Team collaboration and knowledge sharing", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Collaboration Index", "80%", "+5%", "🗣️"), width=4),
    ]),

    dcc.Graph(
        figure=px.line(get_communication_data(), x='Month', y='Collaboration', title="Collaboration Over Time")
    )
])
