import os
import sys
from pathlib import Path

import dash
import dash_bootstrap_components as dbc
# Make sure the project root directory is in the Python path
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent  # Go up one level from app/
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Now the imports will work properly when run directly
from app.app_routes import layout, register_callbacks
import app.layouts.dora.deployment_frequency

print(">>> deployment_frequency.py is being imported!")

# Initialize the Dash app with Bootstrap
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,  # For dynamic layouts
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
    title="AI Metrics Dashboard"
)

# Custom HTML template for the app
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

# Main layout
app.layout = layout

# Register callbacks
register_callbacks(app)

# Initialize the server
server = app.server

def main():
    """Entry point for the application"""
    print("Starting AI Metrics Dashboard...")
    print("Access the dashboard at http://127.0.0.1:8050/")
    app.run(debug=True, port=8050)
    
# Run the app
if __name__ == "__main__":
    main()

def update_deployment_graph(selected_teams):
    print("🚨 CALLBACK TRIGGERED")
    df = get_deployment_frequency_data()
    print("📊 DataFrame preview:\n", df.head())
    print("Columns:", df.columns)
    print("Selected teams:", selected_teams)
    if df.empty:
        print("⚠️ No data returned from get_deployment_frequency_data()")
        return px.bar(title="No Data Available")
    filtered_df = df[df['team_id'].isin(selected_teams)]
    print("Filtered DataFrame:\n", filtered_df)
    return px.bar(
        filtered_df,
        x='Month',
        y='Frequency',
        color='team_id',
        barmode='group',
        title="Deployment Frequency by Team"
    )