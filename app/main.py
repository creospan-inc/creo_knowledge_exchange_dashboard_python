from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}]
)

# 👇 Add this block right here:
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>AI Adoption Metrics Dashboard</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
            <!-- Removed theme-setting script -->
        </footer>
    </body>
</html>
'''

# 🔁 Then continue as normal:
from .app_routes import layout, register_callbacks
app.layout = layout
register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)