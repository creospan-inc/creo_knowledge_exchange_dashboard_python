from dash import html, dcc
import dash_bootstrap_components as dbc
from app.data.metrics_data import efficiency_trend_data
import plotly.express as px
from app.components.helpers import create_metric_card

layout = html.Div([
    html.H1("Efficiency", className="main-header mb-2"),
    html.P("Time saved and overhead reduction from AI", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(create_metric_card("Time Saved", "48 hrs", "+33%", "⏳"), width=4),
        dbc.Col(create_metric_card("Productive Hours", "34 hrs", "+9%", "💡"), width=4),
    ]),

    dcc.Graph(
        figure=px.line(
            efficiency_trend_data,
            x='Month',
            y=['Time Saved', 'Productive Hours'],
            title="Efficiency Over Time"
        ).update_layout(height=400)
    )
])