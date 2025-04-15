import dash
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash_iconify import DashIconify

# Sample data
deployment_data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Deployment Frequency': [2.4, 2.8, 3.1, 3.3, 3.6, 3.9, 4.2],
    'Lead Time': [4.8, 4.5, 4.2, 4.0, 3.8, 3.7, 3.5],
    'Team Satisfaction': [65, 68, 72, 75, 78, 80, 85],
    'AI Adoption': [42, 48, 53, 58, 62, 65, 68]
})

efficiency_data = pd.DataFrame({
    'task': ['Code Review', 'Testing', 'Documentation', 'Bug Fixing', 'Feature Dev'],
    'Traditional': [120, 180, 150, 200, 300],
    'AI-Assisted': [45, 90, 60, 100, 180]
})

activities = [
    {
        'user': 'Alex Johnson',
        'type': 'ai-prompt',
        'description': 'Generated test cases using AI assistant',
        'time': '2 hours ago',
        'icon': 'lucide:code-2'
    },
    {
        'user': 'Sarah Miller',
        'type': 'commit',
        'description': 'Committed AI-generated code refactoring',
        'time': '3 hours ago',
        'icon': 'lucide:git-commit'
    },
    {
        'user': 'David Chen',
        'type': 'pull-request',
        'description': 'Opened PR for AI-assisted feature implementation',
        'time': '5 hours ago',
        'icon': 'lucide:git-pull-request'
    },
    {
        'user': 'Emily Wilson',
        'type': 'comment',
        'description': 'Discussed AI adoption strategy in team meeting',
        'time': '1 day ago',
        'icon': 'lucide:message-square'
    },
    {
        'user': 'Michael Brown',
        'type': 'ai-prompt',
        'description': 'Used AI to optimize database queries',
        'time': '1 day ago',
        'icon': 'lucide:code-2'
    }
]

# Initialize the Dash app with Bootstrap dark theme
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)

# App layout
app.layout = html.Div([
    # Theme toggle
    html.Div([
        dbc.Button(
            html.I(className="bi bi-moon"),
            id="theme-toggle",
            color="light",
            outline=True,
            size="sm",
            className="ms-auto"
        ),
    ], className="d-flex justify-content-end p-3"),

    # Dashboard header
    dbc.Container([
        html.Div([
            html.Div([
                html.H1("AI Adoption Metrics Dashboard", className="mb-1"),
                html.P("Track your team's progress and efficiencies in adopting AI", className="text-muted"),
            ]),
            html.Div([
                dbc.Button("Download Report", color="light", outline=True, className="me-2"),
                dbc.Button("Configure Metrics", color="primary"),
            ], className="d-flex")
        ], className="d-flex justify-content-between align-items-center mb-4"),

        # Tabs
        dbc.Tabs([
            # Overview Tab
            dbc.Tab(label="Overview", tab_id="overview", children=[
                # Metric cards
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.H6("Deployment Frequency", className="card-subtitle mb-2 text-muted"),
                                    DashIconify(icon="lucide:git-pull-request", width=20, className="text-muted"),
                                ], className="d-flex justify-content-between"),
                                html.H3("4.2/week", className="card-title"),
                                html.P("+20.1% from last month", className="card-text small text-muted"),
                            ])
                        ], className="h-100")
                    ], width=12, md=6, lg=3, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.H6("Lead Time for Changes", className="card-subtitle mb-2 text-muted"),
                                    DashIconify(icon="lucide:clock", width=20, className="text-muted"),
                                ], className="d-flex justify-content-between"),
                                html.H3("3.5 days", className="card-title"),
                                html.P("-15.2% from last month", className="card-text small text-muted"),
                            ])
                        ], className="h-100")
                    ], width=12, md=6, lg=3, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.H6("Team Satisfaction", className="card-subtitle mb-2 text-muted"),
                                    DashIconify(icon="lucide:users", width=20, className="text-muted"),
                                ], className="d-flex justify-content-between"),
                                html.H3("85%", className="card-title"),
                                html.P("+5% from last survey", className="card-text small text-muted"),
                            ])
                        ], className="h-100")
                    ], width=12, md=6, lg=3, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([
                                    html.H6("AI Adoption Rate", className="card-subtitle mb-2 text-muted"),
                                    DashIconify(icon="lucide:code-2", width=20, className="text-muted"),
                                ], className="d-flex justify-content-between"),
                                html.H3("68%", className="card-title"),
                                html.P("+12.3% from last quarter", className="card-text small text-muted"),
                            ])
                        ], className="h-100")
                    ], width=12, md=6, lg=3, className="mb-4"),
                ]),

                # Charts
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader(html.H5("Metrics Overview")),
                            dbc.CardBody([
                                dcc.Graph(
                                    id='metrics-overview',
                                    figure=px.line(
                                        deployment_data,
                                        x='month',
                                        y=['Deployment Frequency', 'Lead Time', 'Team Satisfaction', 'AI Adoption'],
                                        labels={'value': 'Value', 'variable': 'Metric'},
                                        template='plotly'
                                    )
                                )
                            ])
                        ], className="h-100")
                    ], width=12, lg=7, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Team Efficiency"),
                                html.P("Comparing AI-assisted vs traditional workflows",
                                       className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                dcc.Graph(
                                    id='team-efficiency',
                                    figure=px.bar(
                                        efficiency_data,
                                        x='task',
                                        y=['Traditional', 'AI-Assisted'],
                                        barmode='group',
                                        labels={'value': 'Minutes', 'variable': 'Workflow'},
                                        template='plotly'
                                    )
                                )
                            ])
                        ], className="h-100")
                    ], width=12, lg=5, className="mb-4"),
                ]),

                # Recent Activity
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Recent Activity"),
                                html.P("Latest AI adoption activities across teams", className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    html.Div([
                                        html.Div([
                                            html.Div(
                                                html.Span(activity['user'][0:2], className="text-center"),
                                                className="avatar bg-light text-dark rounded-circle d-flex align-items-center justify-content-center me-3"
                                            ),
                                            html.Div([
                                                html.Div([
                                                    html.Span(activity['user'], className="fw-medium me-2"),
                                                    DashIconify(icon=activity['icon'], width=16,
                                                                className="text-muted"),
                                                ], className="d-flex align-items-center"),
                                                html.P(activity['description'], className="text-muted small mb-1"),
                                                html.P(activity['time'], className="text-muted small mb-0"),
                                            ])
                                        ], className="d-flex mb-3")
                                    ]) for activity in activities
                                ]),
                                dbc.Button([
                                    "View All Activity ",
                                    DashIconify(icon="lucide:arrow-up-right", width=16)
                                ], color="light", outline=True, className="w-100 mt-2")
                            ])
                        ], className="h-100")
                    ], width=12, className="mb-4"),
                ]),
            ], className="pt-3"),

            # DORA Metrics Tab
            dbc.Tab(label="DORA Metrics", tab_id="dora", children=[
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Deployment Frequency"),
                                html.P("How often your organization successfully deploys to production",
                                       className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:bar-chart-3", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Lead Time for Changes"),
                                html.P("Time it takes for code to go from commit to production",
                                       className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:line-chart", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Change Failure Rate"),
                                html.P("Percentage of deployments causing a failure in production",
                                       className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:bar-chart-3", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Time to Restore Service"),
                                html.P("How long it takes to recover from a failure in production",
                                       className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:line-chart", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, className="mb-4"),
                ])
            ], className="pt-3"),

            # SPACE Metrics Tab
            dbc.Tab(label="SPACE Metrics", tab_id="space", children=[
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Satisfaction"),
                                html.P("Developer satisfaction with AI tools and processes",
                                       className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:bar-chart-3", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, lg=4, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Performance"),
                                html.P("Quality and impact of AI-assisted work", className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:line-chart", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, lg=4, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Activity"),
                                html.P("Volume and types of AI-assisted work", className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:bar-chart-3", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, lg=4, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Communication"),
                                html.P("How AI affects team collaboration", className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:line-chart", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, lg=6, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Efficiency"),
                                html.P("Time saved through AI adoption", className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:bar-chart-3", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, lg=6, className="mb-4"),
                ])
            ], className="pt-3"),

            # Agile Metrics Tab
            dbc.Tab(label="Agile Metrics", tab_id="agile", children=[
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Velocity"),
                                html.P("Story points completed per sprint with AI assistance",
                                       className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:line-chart", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Cycle Time"),
                                html.P("Time from task start to completion", className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:bar-chart-3", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("Sprint Burndown"),
                                html.P("Work remaining vs time in sprint", className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:line-chart", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, className="mb-4"),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader([
                                html.H5("AI Adoption by Story Type"),
                                html.P("AI usage across different types of work", className="text-muted small mb-0")
                            ]),
                            dbc.CardBody([
                                html.Div([
                                    DashIconify(icon="lucide:bar-chart-3", width=64, className="text-muted")
                                ], className="d-flex justify-content-center align-items-center",
                                    style={"height": "300px"})
                            ])
                        ], className="h-100")
                    ], width=12, md=6, className="mb-4"),
                ])
            ], className="pt-3"),
        ], id="tabs", active_tab="overview"),
    ], fluid=True, className="py-4"),
], id="main-container")


# Callback for theme toggle
@callback(
    Output("main-container", "className"),
    Input("theme-toggle", "n_clicks"),
    State("main-container", "className"),
    prevent_initial_call=True
)
def toggle_theme(n_clicks, current_class):
    if current_class == "bg-dark text-light":
        return ""
    else:
        return "bg-dark text-light"


# Callback to update theme toggle icon
@callback(
    Output("theme-toggle", "children"),
    Input("main-container", "className")
)
def update_toggle_icon(current_class):
    if current_class == "bg-dark text-light":
        return html.I(className="bi bi-sun")
    else:
        return html.I(className="bi bi-moon")


if __name__ == '__main__':
    app.run(debug=True)