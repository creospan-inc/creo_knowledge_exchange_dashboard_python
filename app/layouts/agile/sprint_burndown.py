from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import sprint_burndown_data
import plotly.express as px
from app.components.helpers import create_metric_card


layout = html.Div([
    html.H1("Sprint Burndown", className="main-header mb-2"),
    html.P("Work remaining throughout a sprint", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Remaining Points", "8", "Sprint end", "📉"), width=4),
    ]),

    dcc.Graph(
        figure=px.line(sprint_burndown_data, x='Day', y='Remaining', title="Sprint Burndown Chart")
    )
])
