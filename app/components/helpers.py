import dash_bootstrap_components as dbc
from dash import html

def create_metric_card(title, value, delta, icon, is_dark=False):
    delta_class = "metric-delta-up" if "+" in delta else "metric-delta-down" if "-" in delta else "metric-delta"
    return dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(html.Div(title, className="fw-medium"), width=10),
                dbc.Col(html.Div(icon), width=2),
            ]),
            html.Div(value, className="metric-value mt-2"),
            html.Div(delta, className=f"metric-delta {delta_class}"),
        ]),
        className="card h-100" + (" card-dark" if is_dark else "")
    )
