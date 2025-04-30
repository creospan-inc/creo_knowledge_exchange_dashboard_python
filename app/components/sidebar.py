from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Div([
            html.H4("📊  AI Metrics", className="d-inline-block ms-2 mb-4"),
        ], className="d-flex align-items-center"),

        # html.Button(
        #     id="theme-toggle",
        #     children="🌙",
        #     className="btn btn-outline-secondary mb-3",
        #     style={"width": "40px"}
        # ),

        html.H6("Navigation", className="nav-header"),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/", id="dashboard-link", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),

        html.H6("AI Metrics", className="nav-header"),
        dbc.Nav(
            [
                dbc.NavLink("Time Saving by Role", href="/ai/time-saving-by-role", id="time-saving-by-role-link", active="exact"),
                dbc.NavLink("AI Adoption", href="/agile/ai-adoption", id="ai-adoption-link", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),

        html.H6("DORA Metrics", className="nav-header"),
        dbc.Nav(
            [
                dbc.NavLink("Deployment Frequency", href="/dora/deployment-frequency", id="deployment-frequency-link", active="exact"),
                dbc.NavLink("Lead Time for Changes", href="/dora/lead-time", id="lead-time-link", active="exact"),
                dbc.NavLink("Change Failure Rate", href="/dora/change-failure-rate", id="change-failure-rate-link", active="exact"),
                dbc.NavLink("Time to Restore", href="/dora/time-to-restore", id="time-to-restore-link", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),

        html.H6("SPACE Metrics", className="nav-header"),
        dbc.Nav(
            [
                dbc.NavLink("Satisfaction", href="/space/satisfaction", id="satisfaction-link", active="exact"),
                dbc.NavLink("Performance", href="/space/performance", id="performance-link", active="exact"),
                dbc.NavLink("Activity", href="/space/activity", id="activity-link", active="exact"),
                dbc.NavLink("Communication", href="/space/communication", id="communication-link", active="exact"),
                dbc.NavLink("Efficiency", href="/space/efficiency", id="efficiency-link", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),

        html.H6("Agile Metrics", className="nav-header"),
        dbc.Nav(
            [
                dbc.NavLink("Velocity", href="/agile/velocity", id="velocity-link", active="exact"),
                dbc.NavLink("Cycle Time", href="/agile/cycle-time", id="cycle-time-link", active="exact"),
                dbc.NavLink("Sprint Burndown", href="/agile/sprint-burndown", id="sprint-burndown-link", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),

        dbc.Nav(
            [
                dbc.NavLink("Settings", href="/settings", id="settings-link", active="exact"),
            ],
            vertical=True,
            pills=True,
            className="mt-3",
        ),
    ],
    className="sidebar",
)