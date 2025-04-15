from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import velocity_data
import plotly.express as px
from app.components.helpers import create_metric_card


layout = html.Div([
    html.H1("Velocity", className="main-header mb-2"),
    html.P("Completed work per sprint", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Current Velocity", "36 pts", "+12%", "🚀"), width=4),
    ]),

    dcc.Graph(
        figure=px.bar(velocity_data, x='Sprint', y='Velocity', title="Sprint Velocity")
    )
])
