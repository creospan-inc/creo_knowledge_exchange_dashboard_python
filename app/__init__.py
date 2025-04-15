import dash
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}]
)

# Custom index string with your styles
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>AI Adoption Metrics Dashboard</title>
        {%favicon%}
        {%css%}
        <style>
            .main-header {
                font-size: 30px;
                font-weight: bold;
            }
            .card {
                padding: 20px;
                border-radius: 10px;
                background-color: #f8f9fa;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                margin-bottom: 15px;
                height: 100%;
            }
            .card-dark {
                background-color: #262730;
                color: #ffffff;
            }
            .metric-value {
                font-size: 28px;
                font-weight: bold;
            }
            .metric-delta {
                font-size: 12px;
                color: #6c757d;
            }
            .metric-delta-up {
                color: #28a745;
            }
            .metric-delta-down {
                color: #dc3545;
            }
            .section-header {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .subsection-header {
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 8px;
            }
            .dark-theme {
                background-color: #121212;
                color: #ffffff;
            }
            .dark-theme .card {
                background-color: #262730;
                color: #ffffff;
            }
            .dark-theme .navbar {
                background-color: #1e1e1e !important;
            }
            .sidebar {
                height: 100vh;
                position: fixed;
                top: 0;
                left: 0;
                padding: 20px;
                width: 250px;
                z-index: 1;
                overflow-y: auto;
                background-color: #f8f9fa;
                border-right: 1px solid #dee2e6;
            }
            .dark-theme .sidebar {
                background-color: #1e1e1e;
                border-right: 1px solid #444;
            }
            .content {
                margin-left: 250px;
                padding: 20px;
            }
            .nav-link {
                padding: 8px 16px;
                margin: 4px 0;
                border-radius: 4px;
            }
            .nav-link:hover {
                background-color: rgba(0, 0, 0, 0.05);
            }
            .dark-theme .nav-link:hover {
                background-color: rgba(255, 255, 255, 0.05);
            }
            .nav-link.active {
                background-color: #007bff;
                color: white;
            }
            .nav-header {
                font-size: 14px;
                font-weight: bold;
                text-transform: uppercase;
                margin-top: 16px;
                margin-bottom: 8px;
                color: #6c757d;
            }
            .dark-theme .nav-header {
                color: #adb5bd;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''