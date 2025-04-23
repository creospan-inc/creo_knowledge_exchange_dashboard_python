from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash.exceptions

from .components.sidebar import sidebar
from .layouts.dashboard import dashboard_layout

# DORA Metrics
from .layouts.dora.deployment_frequency import layout as dora_deployment_frequency_layout
from .layouts.dora.lead_time import layout as dora_lead_time_layout
from .layouts.dora.failure_rate import layout as dora_change_failure_rate_layout
from .layouts.dora.restore_time import layout as dora_time_to_restore_layout

# SPACE Metrics
from .layouts.space.satisfaction import layout as space_satisfaction_layout
from .layouts.space.performance import layout as space_performance_layout
from .layouts.space.activity import layout as space_activity_layout
from .layouts.space.communication import layout as space_communication_layout
from .layouts.space.efficiency import layout as space_efficiency_layout

# Agile Metrics
from .layouts.agile.velocity import layout as agile_velocity_layout
from .layouts.agile.cycle_time import layout as agile_cycle_time_layout
from .layouts.agile.sprint_burndown import layout as agile_sprint_burndown_layout
from .layouts.agile.ai_adoption import layout as agile_ai_adoption_layout

# AI Metrics
from .layouts.ai.time_saving_by_role import layout as ai_time_saving_by_role_layout

# Settings
from .layouts.settings import layout as settings_layout

# Ensure callbacks in dashboard.py are registered
from .layouts import dashboard

# 🌐 Main layout structure
layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='theme-store', data={'theme': 'light'}),

    # Theme toggle button bar
    html.Div([
        html.Button("🌙", id="theme-toggle", n_clicks=0, className="btn btn-outline-secondary me-2"),
    ], className="d-flex justify-content-end p-2 border-bottom"),

    # Dynamic content container with theme class
    html.Div([
        html.Div(id='page-content', className='content')
    ], className='light-theme', id='main-container')
])


# 🔁 Register routing and theming callbacks
def register_callbacks(app):
    # Page rendering and theme class application
    @app.callback(
        Output('page-content', 'children'),
        Output('main-container', 'className'),
        Input('url', 'pathname'),
        Input('theme-store', 'data')
    )
    def display_page(pathname, theme_data):
        print(f"DISPLAY_PAGE - Path: {pathname}, Theme data: {theme_data}")
        theme_class = 'dark-theme' if theme_data and theme_data.get('theme') == 'dark' else 'light-theme'
        print(f"DISPLAY_PAGE - Applying class: '{theme_class}'")

        content = [sidebar]

        # Dashboard
        if pathname in ['/', '']:
            content.append(dashboard_layout)

        # AI Metrics
        elif pathname == '/ai/time-saving-by-role':
            content.append(ai_time_saving_by_role_layout)

        # DORA Metrics
        elif pathname == '/dora/deployment-frequency':
            content.append(dora_deployment_frequency_layout)
        elif pathname == '/dora/lead-time':
            content.append(dora_lead_time_layout)
        elif pathname == '/dora/change-failure-rate':
            content.append(dora_change_failure_rate_layout)
        elif pathname == '/dora/time-to-restore':
            content.append(dora_time_to_restore_layout)

        # SPACE Metrics
        elif pathname == '/space/satisfaction':
            content.append(space_satisfaction_layout)
        elif pathname == '/space/performance':
            content.append(space_performance_layout)
        elif pathname == '/space/activity':
            content.append(space_activity_layout)
        elif pathname == '/space/communication':
            content.append(space_communication_layout)
        elif pathname == '/space/efficiency':
            content.append(space_efficiency_layout)

        # Agile Metrics
        elif pathname == '/agile/velocity':
            content.append(agile_velocity_layout)
        elif pathname == '/agile/cycle-time':
            content.append(agile_cycle_time_layout)
        elif pathname == '/agile/sprint-burndown':
            content.append(agile_sprint_burndown_layout)
        elif pathname == '/agile/ai-adoption':
            content.append(agile_ai_adoption_layout)

        # Settings
        elif pathname == '/settings':
            content.append(settings_layout)

        # Fallback for unknown routes
        else:
            content.append(html.Div([
                html.H1("Page Not Found", className="main-header"),
                html.P(f"No content found for {pathname}", className="text-muted"),
                html.A("Return to Dashboard", href="/", className="btn btn-primary mt-2")
            ]))

        return content, theme_class

    # Theme toggle handler with protection from phantom triggers
    @app.callback(
        Output('theme-store', 'data'),
        Input('theme-toggle', 'n_clicks'),
        State('theme-store', 'data'),
        prevent_initial_call=True
    )
    def toggle_theme(n_clicks, current_theme_data):
        print(f"TOGGLE_THEME - Clicked: {n_clicks}, Current data: {current_theme_data}")

        if n_clicks is None:
            raise dash.exceptions.PreventUpdate

        current_theme = current_theme_data.get('theme', 'light') if current_theme_data else 'light'
        new_theme = 'dark' if current_theme == 'light' else 'light'
        print(f"TOGGLE_THEME - New theme: {new_theme}")
        return {'theme': new_theme}

    # Keep the icon in sync with current theme state
    @app.callback(
        Output('theme-toggle', 'children'),
        Input('theme-store', 'data'),
        prevent_initial_call=True
    )
    def update_toggle_icon(theme_data):
        if theme_data.get('theme') == 'dark':
            return '☀️'
        return '🌙'