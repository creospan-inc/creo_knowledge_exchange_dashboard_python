from dash import html, dcc
from dash.dependencies import Input, Output
from app.components.sidebar import sidebar

# Import layouts from your different metric sections
from layouts.dashboard import dashboard_layout

# DORA Metrics
from layouts.dora.deployment_frequency import layout as dora_deployment_frequency_layout
from layouts.dora.lead_time import layout as dora_lead_time_layout
from layouts.dora.failure_rate import layout as dora_change_failure_rate_layout
from layouts.dora.restore_time import layout as dora_time_to_restore_layout

# SPACE Metrics
from layouts.space.satisfaction import layout as space_satisfaction_layout
from layouts.space.performance import layout as space_performance_layout
from layouts.space.activity import layout as space_activity_layout
from layouts.space.communication import layout as space_communication_layout
from layouts.space.efficiency import layout as space_efficiency_layout

# Agile Metrics
from layouts.agile.velocity import layout as agile_velocity_layout
from layouts.agile.cycle_time import layout as agile_cycle_time_layout
from layouts.agile.sprint_burndown import layout as agile_sprint_burndown_layout
from layouts.agile.ai_adoption import layout as agile_ai_adoption_layout

# Settings (Optional)
from layouts.settings import layout as settings_layout  # If you have a settings page

# app/app_routes.py
from layouts import dashboard  # 👈 This line ensures callbacks in dashboard.py are registered
# 🌐 Main layout structure with routing
layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='theme-store', data={'theme': 'light'}),
    html.Div(id='page-content', className='content')
], id='main-container')


# 🔁 Routing callback
def register_callbacks(app):
    @app.callback(
        Output('page-content', 'children'),
        Output('main-container', 'className'),
        Input('url', 'pathname'),
        Input('theme-store', 'data')
    )
    def display_page(pathname, theme_data):
        theme_class = 'dark-theme' if theme_data.get('theme') == 'dark' else ''
        content = [sidebar]

        # Dashboard
        if pathname in ['/', '']:
            content.append(dashboard_layout)

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