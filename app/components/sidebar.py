from dash import html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Div([
            html.H4("📊  AI Metrics", className="d-inline-block ms-2 mb-4"),
        ], className="d-flex align-items-center"),

        # Navigation Section
        dbc.Button("Navigation ▾", id="toggle-nav", className="mb-2", color="link"),
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Dashboard", href="/", id="dashboard-link", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse-nav",
            is_open=True,
        ),

        # AI Metrics Section
        dbc.Button("AI Metrics ▾", id="toggle-ai", className="mb-2", color="link"),
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Time Saving by Role", href="/ai/time-saving-by-role", id="time-saving-by-role-link", active="exact"),
                    dbc.NavLink("Sentiment Score", href="/ai/ai-adoption", id="sentiment-score-link", active="exact"),
                    dbc.NavLink("ROI", href="/ai/roi", id="roi-link", active="exact"),
                    dbc.NavLink("Adoption %", href="/ai/adoption-percentage", id="agile-team-adoption-percent-link", active="exact"),
                    dbc.NavLink("Maturity Stage", href="/ai/maturity-stage", id="maturity-stage-link", active="exact"),
                    dbc.NavLink("Model Performance", href="/ai/model-performance", id="velocity-link", active="exact"),
                    dbc.NavLink("User Engagement", href="/ai/user-engagement", id="user-engagement-link", active="exact"),
                    dbc.NavLink("Cost to Serve", href="/ai/cost-to-serve", id="sprint-burndown-link", active="exact"),
                    dbc.NavLink("Risk/Compliance", href="/ai/sprint-burndown", id="sprint-burndown-link", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse-ai",
            is_open=True,
        ),

        # DORA Metrics Section
        dbc.Button("DORA Metrics ▾", id="toggle-dora", className="mb-2", color="link"),
        dbc.Collapse(
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
            id="collapse-dora",
            is_open=True,
        ),

        # SPACE Metrics Section
        dbc.Button("SPACE Metrics ▾", id="toggle-space", className="mb-2", color="link"),
        dbc.Collapse(
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
            id="collapse-space",
            is_open=True,
        ),

        # Agile Metrics Section
        dbc.Button("Agile Metrics ▾", id="toggle-agile", className="mb-2", color="link"),
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Velocity", href="/agile/velocity", id="velocity-link", active="exact"),
                    dbc.NavLink("Cycle Time", href="/agile/cycle-time", id="cycle-time-link", active="exact"),
                    dbc.NavLink("Sprint Burndown", href="/agile/sprint-burndown", id="sprint-burndown-link", active="exact"),
                    dbc.NavLink("Adoption %", href="/agile/agile_team_adoption-percent",id="agile-team-adoption-percent-link", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse-agile",
            is_open=True,
        ),

        # Settings
        html.Hr(),
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