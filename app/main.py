from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}]
)

# ✅ Only import this AFTER the app is created
from app.app_routes import layout, register_callbacks

app.layout = layout
register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)