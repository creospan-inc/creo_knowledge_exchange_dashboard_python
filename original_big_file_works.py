import dash
from dash import dcc, html, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}])

# Custom CSS for styling
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

# Sample data for all visualizations
metrics_data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Deployment Frequency': [2.4, 2.8, 3.1, 3.3, 3.6, 3.9, 4.2],
    'Lead Time': [4.8, 4.5, 4.2, 4.0, 3.8, 3.7, 3.5],
    'Team Satisfaction': [65, 68, 72, 75, 78, 80, 85],
    'AI Adoption': [42, 48, 53, 58, 62, 65, 68]
})

team_efficiency_data = pd.DataFrame({
    'Task': ['Code Review', 'Testing', 'Documentation', 'Bug Fixing', 'Feature Dev'],
    'Traditional': [120, 180, 150, 200, 300],
    'AI-Assisted': [45, 90, 60, 100, 180]
})

activities_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'user': ['Alex Johnson', 'Sarah Miller', 'David Chen', 'Emily Wilson', 'Michael Brown'],
    'type': ['ai-prompt', 'commit', 'pull-request', 'comment', 'ai-prompt'],
    'description': [
        'Generated test cases using AI assistant',
        'Committed AI-generated code refactoring',
        'Opened PR for AI-assisted feature implementation',
        'Discussed AI adoption strategy in team meeting',
        'Used AI to optimize database queries'
    ],
    'time': ['2 hours ago', '3 hours ago', '5 hours ago', '1 day ago', '1 day ago']
})

# DORA Metrics data
failure_rate_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Rate': [18.5, 17.2, 16.8, 15.3, 14.1, 13.2, 12.5]
})

restore_time_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Hours': [7.5, 6.8, 6.2, 5.5, 5.0, 4.6, 4.2]
})

# SPACE Metrics data
satisfaction_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Score': [65, 68, 72, 75, 78, 80, 85],
    'Benchmark': [62, 62, 63, 63, 64, 64, 65]
})

satisfaction_categories = pd.DataFrame({
    'Category': ['AI Tools', 'Work Environment', 'Team Collaboration', 'Development Process', 'Career Growth'],
    'Score': [88, 82, 85, 78, 80],
    'Change': ['+8%', '+5%', '+7%', '+4%', '+6%']
})

performance_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Quality Score': [72, 75, 78, 82, 85, 88, 92],
    'Impact Score': [68, 70, 73, 76, 80, 83, 87],
    'Benchmark': [70, 70, 71, 71, 72, 72, 73]
})

quality_metrics = pd.DataFrame({
    'Metric': ['Code Quality', 'Test Coverage', 'Bug Density', 'Documentation', 'Maintainability'],
    'Traditional': [76, 68, 12, 65, 72],
    'AI-Assisted': [89, 85, 5, 87, 90],
    'Change': ['+17%', '+25%', '-58%', '+34%', '+25%']
})

activity_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'AI Prompts': [120, 150, 180, 210, 240, 270, 300],
    'Commits': [180, 195, 210, 225, 240, 255, 270],
    'PRs': [45, 50, 55, 60, 65, 70, 75],
    'Reviews': [90, 100, 110, 120, 130, 140, 150]
})

communication_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Collaboration Index': [68, 72, 75, 78, 82, 85, 88],
    'Meeting Efficiency': [65, 68, 72, 75, 78, 82, 85],
    'Knowledge Sharing': [72, 75, 78, 80, 83, 86, 90]
})

communication_channels = pd.DataFrame({
    'Channel': ['Team Meetings', 'Code Reviews', 'Documentation', 'Knowledge Base', 'Pair Programming'],
    'Traditional': [4.2, 3.5, 8.5, 6.2, 5.8],
    'AI-Assisted': [2.8, 1.8, 3.5, 2.5, 3.2],
    'Change': ['-33%', '-49%', '-59%', '-60%', '-45%']
})

efficiency_trend_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Time Saved': [12, 18, 24, 30, 36, 42, 48],
    'Productive Hours': [22, 24, 26, 28, 30, 32, 34],
    'Overhead': [18, 16, 14, 12, 10, 8, 6]
})

efficiency_by_activity = pd.DataFrame({
    'Activity': ['Code Writing', 'Code Review', 'Testing', 'Documentation', 'Meetings'],
    'Time Saved %': [35, 42, 50, 60, 25],
    'Hours Per Week': [8.5, 6.2, 7.5, 4.5, 5.0]
})

# Agile Metrics data
velocity_data = pd.DataFrame({
    'Sprint': ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4', 'Sprint 5', 'Sprint 6', 'Sprint 7'],
    'Planned': [28, 32, 35, 38, 42, 45, 48],
    'Completed': [25, 30, 34, 36, 40, 44, 48],
    'AI-Assisted': [15, 18, 22, 25, 30, 35, 40]
})

velocity_by_team = pd.DataFrame({
    'Team': ['Frontend', 'Backend', 'DevOps', 'QA', 'Mobile'],
    'Velocity': [18, 22, 15, 12, 16],
    'AI Percentage': [75, 82, 68, 85, 72],
    'Predictability': [92, 95, 90, 94, 88]
})

cycle_time_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Traditional': [8.5, 8.2, 7.8, 7.5, 7.2, 6.8, 6.5],
    'AI-Assisted': [5.2, 4.8, 4.5, 4.2, 3.9, 3.6, 3.2]
})

cycle_time_breakdown = pd.DataFrame({
    'Stage': ['Planning', 'Development', 'Code Review', 'Testing', 'Deployment'],
    'Traditional': [1.5, 3.2, 1.2, 1.8, 0.8],
    'AI-Assisted': [0.8, 1.5, 0.5, 0.8, 0.4]
})

sprint_burndown_data = pd.DataFrame({
    'Day': [f'Day {i}' for i in range(1, 11)],
    'Remaining': [48, 45, 42, 38, 35, 30, 28, 22, 15, 0],
    'Ideal': [48, 43.2, 38.4, 33.6, 28.8, 24, 19.2, 14.4, 9.6, 4.8]
})

sprint_comparison_data = pd.DataFrame({
    'Sprint': ['Sprint 3', 'Sprint 4', 'Sprint 5', 'Sprint 6', 'Sprint 7'],
    'AI Adoption': [45, 55, 65, 75, 85],
    'Burndown Index': [0.82, 0.85, 0.88, 0.92, 0.95]
})

ai_adoption_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
    'Adoption': [42, 48, 53, 58, 62, 65, 68],
    'Impact': [35, 40, 45, 52, 58, 62, 65]
})

ai_adoption_by_team = pd.DataFrame({
    'Team': ['Frontend', 'Backend', 'DevOps', 'QA', 'Mobile'],
    'Adoption': [75, 82, 68, 85, 72],
    'Impact': [70, 78, 65, 82, 68],
    'Satisfaction': [85, 88, 80, 90, 82]
})

ai_adoption_tools = pd.DataFrame({
    'Tool': ['GitHub Copilot', 'ChatGPT', 'Claude', 'Midjourney', 'Internal AI Tools'],
    'Adoption Rate': [85, 78, 65, 45, 92],
    'User Satisfaction': [90, 82, 75, 80, 88],
    'Productivity Gain': [45, 38, 32, 25, 52],
    'Primary Use Case': ['Code generation', 'Problem solving', 'Documentation', 'UI mockups', 'Code review']
})


# Helper function to create metric cards
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


# Create the sidebar
sidebar = html.Div(
    [
        html.Div([
            html.Img(src="https://via.placeholder.com/40x40.png?text=⚡", width=40),
            html.H4("AI Metrics", className="d-inline-block ms-2 mb-4"),
        ], className="d-flex align-items-center"),

        html.Button(
            id="theme-toggle",
            children="🌙",
            className="btn btn-outline-secondary mb-3",
            style={"width": "40px"}
        ),

        html.H6("Navigation", className="nav-header"),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/", id="dashboard-link", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),

        html.H6("DORA Metrics", className="nav-header"),
        dbc.Nav(
            [
                dbc.NavLink("Deployment Frequency", href="/dora/deployment-frequency", id="deployment-frequency-link",
                            active="exact"),
                dbc.NavLink("Lead Time for Changes", href="/dora/lead-time", id="lead-time-link", active="exact"),
                dbc.NavLink("Change Failure Rate", href="/dora/change-failure-rate", id="change-failure-rate-link",
                            active="exact"),
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
                dbc.NavLink("Sprint Burndown", href="/agile/sprint-burndown", id="sprint-burndown-link",
                            active="exact"),
                dbc.NavLink("AI Adoption", href="/agile/ai-adoption", id="ai-adoption-link", active="exact"),
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

# Define the layout for the dashboard page
dashboard_layout = html.Div([
    html.H1("AI Adoption Metrics Dashboard", className="main-header mb-2"),
    html.P("Track your team's progress and efficiencies in adopting AI", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col(width=8),
        dbc.Col(
            dbc.Button("Download Report", color="primary", outline=True, className="me-2"),
            width=2,
            className="d-flex justify-content-end"
        ),
        dbc.Col(
            dbc.Button("Configure Metrics", color="primary"),
            width=2,
            className="d-flex justify-content-end"
        ),
    ], className="mb-4"),

    dbc.Tabs([
        dbc.Tab(label="Overview", tab_id="overview", children=[
            dbc.Row([
                dbc.Col(create_metric_card("Deployment Frequency", "4.2/week", "+20.1% from last month", "🔄"), width=3),
                dbc.Col(create_metric_card("Lead Time for Changes", "3.5 days", "-15.2% from last month", "⏱️"),
                        width=3),
                dbc.Col(create_metric_card("Team Satisfaction", "85%", "+5% from last survey", "👥"), width=3),
                dbc.Col(create_metric_card("AI Adoption Rate", "68%", "+12.3% from last quarter", "🤖"), width=3),
            ], className="mb-4"),

            dbc.Row([
                dbc.Col([
                    html.H5("Metrics Overview", className="section-header"),
                    dcc.Graph(
                        figure=px.line(
                            metrics_data,
                            x='month',
                            y=['Deployment Frequency', 'Lead Time', 'Team Satisfaction', 'AI Adoption'],
                            title='Metrics Trends'
                        ).update_layout(height=400)
                    )
                ], width=8),

                dbc.Col([
                    html.H5("Team Efficiency", className="section-header"),
                    html.P("Comparing AI-assisted vs traditional workflows", className="subsection-header"),
                    dcc.Graph(
                        figure=go.Figure(data=[
                            go.Bar(name='Traditional', x=team_efficiency_data['Task'],
                                   y=team_efficiency_data['Traditional'], marker_color='#8884d8'),
                            go.Bar(name='AI-Assisted', x=team_efficiency_data['Task'],
                                   y=team_efficiency_data['AI-Assisted'], marker_color='#82ca9d')
                        ]).update_layout(
                            title='Time Spent on Tasks (Minutes)',
                            barmode='group',
                            height=400
                        )
                    )
                ], width=4),
            ], className="mb-4"),

            html.H5("Recent Activity", className="section-header"),
            html.P("Latest AI adoption activities across teams", className="subsection-header"),

            dbc.ListGroup([
                dbc.ListGroupItem([
                    dbc.Row([
                        dbc.Col(
                            html.Img(src=f"https://via.placeholder.com/40x40.png?text={activity['user'][0:2]}",
                                     width=40),
                            width=1
                        ),
                        dbc.Col([
                            html.Div(activity['user'], className="fw-bold"),
                            html.Div(activity['description']),
                            html.Small(activity['time'], className="text-muted")
                        ], width=11)
                    ])
                ]) for activity in activities_data.to_dict('records')
            ], className="mb-3"),

            dbc.Button("View All Activity", color="primary", outline=True, className="w-100")
        ]),

        dbc.Tab(label="DORA Metrics", tab_id="dora", children=[
            dbc.Row([
                dbc.Col([
                    html.H5("Deployment Frequency", className="section-header"),
                    html.P("How often your organization successfully deploys to production",
                           className="subsection-header"),
                    dcc.Graph(
                        figure=px.bar(
                            pd.DataFrame({
                                'Month': metrics_data['month'],
                                'Frequency': metrics_data['Deployment Frequency']
                            }),
                            x='Month',
                            y='Frequency',
                            title='Deployments Per Week'
                        ).update_layout(height=350)
                    )
                ], width=6),

                dbc.Col([
                    html.H5("Lead Time for Changes", className="section-header"),
                    html.P("Time it takes for code to go from commit to production", className="subsection-header"),
                    dcc.Graph(
                        figure=px.line(
                            pd.DataFrame({
                                'Month': metrics_data['month'],
                                'Days': metrics_data['Lead Time']
                            }),
                            x='Month',
                            y='Days',
                            title='Lead Time (Days)'
                        ).update_layout(height=350)
                    )
                ], width=6),
            ], className="mb-4"),

            dbc.Row([
                dbc.Col([
                    html.H5("Change Failure Rate", className="section-header"),
                    html.P("Percentage of deployments causing a failure in production", className="subsection-header"),
                    dcc.Graph(
                        figure=px.bar(
                            failure_rate_data,
                            x='Month',
                            y='Rate',
                            title='Failure Rate (%)'
                        ).update_layout(height=350)
                    )
                ], width=6),

                dbc.Col([
                    html.H5("Time to Restore Service", className="section-header"),
                    html.P("How long it takes to recover from a failure in production", className="subsection-header"),
                    dcc.Graph(
                        figure=px.line(
                            restore_time_data,
                            x='Month',
                            y='Hours',
                            title='Time to Restore (Hours)'
                        ).update_layout(height=350)
                    )
                ], width=6),
            ]),
        ]),

        dbc.Tab(label="SPACE Metrics", tab_id="space", children=[
            dbc.Row([
                dbc.Col([
                    html.H5("Satisfaction", className="section-header"),
                    html.P("Developer satisfaction with AI tools and processes", className="subsection-header"),
                    dcc.Graph(
                        figure=px.bar(
                            satisfaction_data,
                            x='Month',
                            y='Score',
                            title='Satisfaction Score (%)'
                        ).update_layout(height=300)
                    )
                ], width=4),

                dbc.Col([
                    html.H5("Performance", className="section-header"),
                    html.P("Quality and impact of AI-assisted work", className="subsection-header"),
                    dcc.Graph(
                        figure=px.line(
                            performance_data,
                            x='Month',
                            y='Quality Score',
                            title='Quality Score (%)'
                        ).update_layout(height=300)
                    )
                ], width=4),

                dbc.Col([
                    html.H5("Activity", className="section-header"),
                    html.P("Volume and types of AI-assisted work", className="subsection-header"),
                    dcc.Graph(
                        figure=px.bar(
                            activity_data,
                            x='Month',
                            y='AI Prompts',
                            title='AI Prompts Count'
                        ).update_layout(height=300)
                    )
                ], width=4),
            ], className="mb-4"),

            dbc.Row([
                dbc.Col([
                    html.H5("Communication", className="section-header"),
                    html.P("How AI affects team collaboration", className="subsection-header"),
                    dcc.Graph(
                        figure=px.line(
                            communication_data,
                            x='Month',
                            y='Collaboration Index',
                            title='Collaboration Index (%)'
                        ).update_layout(height=300)
                    )
                ], width=6),

                dbc.Col([
                    html.H5("Efficiency", className="section-header"),
                    html.P("Time saved through AI adoption", className="subsection-header"),
                    dcc.Graph(
                        figure=px.bar(
                            efficiency_trend_data,
                            x='Month',
                            y='Time Saved',
                            title='Time Saved (Hours/Week)'
                        ).update_layout(height=300)
                    )
                ], width=6),
            ]),
        ]),

        dbc.Tab(label="Agile Metrics", tab_id="agile", children=[
            dbc.Row([
                dbc.Col([
                    html.H5("Velocity", className="section-header"),
                    html.P("Story points completed per sprint with AI assistance", className="subsection-header"),
                    dcc.Graph(
                        figure=px.line(
                            velocity_data,
                            x='Sprint',
                            y='Completed',
                            title='Velocity (Story Points)'
                        ).update_layout(height=350)
                    )
                ], width=6),

                dbc.Col([
                    html.H5("Cycle Time", className="section-header"),
                    html.P("Time from task start to completion", className="subsection-header"),
                    dcc.Graph(
                        figure=px.bar(
                            cycle_time_data,
                            x='Month',
                            y='AI-Assisted',
                            title='Cycle Time (Days)'
                        ).update_layout(height=350)
                    )
                ], width=6),
            ], className="mb-4"),

            dbc.Row([
                dbc.Col([
                    html.H5("Sprint Burndown", className="section-header"),
                    html.P("Work remaining vs time in sprint", className="subsection-header"),
                    dcc.Graph(
                        figure=px.line(
                            sprint_burndown_data,
                            x='Day',
                            y='Remaining',
                            title='Sprint Burndown (Story Points)'
                        ).update_layout(height=350)
                    )
                ], width=6),

                dbc.Col([
                    html.H5("AI Adoption by Team", className="section-header"),
                    html.P("AI usage across different teams", className="subsection-header"),
                    dcc.Graph(
                        figure=px.bar(
                            ai_adoption_by_team,
                            x='Team',
                            y='Adoption',
                            title='AI Adoption by Team (%)'
                        ).update_layout(height=350)
                    )
                ], width=6),
            ]),
        ]),
    ], id="dashboard-tabs", active_tab="overview"),
])


# Define layouts for individual metric pages
def create_dora_deployment_frequency_layout():
    return html.Div([
        html.H1("Deployment Frequency", className="main-header mb-2"),
        html.P("How often your organization successfully deploys to production", className="text-muted mb-4"),

        dbc.Row([
            dbc.Col(create_metric_card("Current Frequency", "4.2/week", "+20.1% from last month", "🔄"), width=4),
            dbc.Col(create_metric_card("Industry Average", "3.5/week", "For companies in your sector", "🔄"), width=4),
            dbc.Col(create_metric_card("Elite Performance", "Multiple/day", "Target for high-performing teams", "🔄"),
                    width=4),
        ], className="mb-4"),

        dbc.Tabs([
            dbc.Tab(label="Overview", tab_id="overview", children=[
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Deployment Frequency", className="section-header"),
                        html.P("Number of deployments per week over time", className="subsection-header"),
                        dcc.Graph(
                            figure=px.bar(
                                pd.DataFrame({
                                    'Month': metrics_data['month'],
                                    'Frequency': metrics_data['Deployment Frequency']
                                }),
                                x='Month',
                                y='Frequency',
                                title='Deployments Per Week'
                            ).update_layout(height=400)
                        )
                    ])
                ),

                dbc.Card(
                    dbc.CardBody([
                        html.H5("Understanding Deployment Frequency", className="section-header"),
                        html.P("What this metric means and how to improve it", className="subsection-header"),

                        html.H6("What is Deployment Frequency?", className="mt-3"),
                        html.P(
                            "Deployment Frequency measures how often an organization successfully releases to production. It's a key indicator of your delivery pipeline's efficiency and your team's ability to deliver small batches of work quickly."),

                        html.H6("Performance Levels", className="mt-3"),
                        html.Ul([
                            html.Li([html.Span("Elite:", className="fw-medium"), " Multiple deployments per day"]),
                            html.Li(
                                [html.Span("High:", className="fw-medium"), " Between once per day and once per week"]),
                            html.Li([html.Span("Medium:", className="fw-medium"),
                                     " Between once per week and once per month"]),
                            html.Li([html.Span("Low:", className="fw-medium"),
                                     " Between once per month and once every six months"]),
                        ]),

                        html.H6("How to Improve", className="mt-3"),
                        html.Ul([
                            html.Li("Implement continuous integration and continuous delivery (CI/CD) pipelines"),
                            html.Li("Break work into smaller, more manageable chunks"),
                            html.Li("Automate testing and deployment processes"),
                            html.Li("Use feature flags to separate deployment from release"),
                            html.Li("Adopt trunk-based development practices"),
                        ]),
                    ])
                ),
            ]),

            dbc.Tab(label="Trends", tab_id="trends"),
            dbc.Tab(label="Raw Data", tab_id="data"),
        ], id="deployment-frequency-tabs", active_tab="overview"),
    ])


def create_space_satisfaction_layout():
    return html.Div([
        html.H1("Developer Satisfaction", className="main-header mb-2"),
        html.P("Measuring how satisfied developers are with AI tools and processes", className="text-muted mb-4"),

        dbc.Row([
            dbc.Col(create_metric_card("Current Satisfaction", "85%", "+5% from last survey", "👥"), width=4),
            dbc.Col(create_metric_card("Industry Average", "65%", "Based on similar organizations", "👥"), width=4),
            dbc.Col(create_metric_card("Response Rate", "92%", "42 out of 46 team members", "👥"), width=4),
        ], className="mb-4"),

        dbc.Tabs([
            dbc.Tab(label="Overview", tab_id="overview", children=[
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Satisfaction Trends", className="section-header"),
                        html.P("Developer satisfaction over time compared to industry benchmark",
                               className="subsection-header"),
                        dcc.Graph(
                            figure=px.line(
                                satisfaction_data,
                                x='Month',
                                y=['Score', 'Benchmark'],
                                title='Satisfaction Score (%)'
                            ).update_layout(height=400)
                        )
                    ])
                ),

                dbc.Card(
                    dbc.CardBody([
                        html.H5("Understanding Developer Satisfaction", className="section-header"),
                        html.P("What this metric means and how to improve it", className="subsection-header"),

                        html.H6("What is Developer Satisfaction?", className="mt-3"),
                        html.P(
                            "Developer Satisfaction measures how content developers are with their tools, processes, work environment, and the adoption of AI in their workflow. This metric reflects the overall experience of developers and can significantly impact productivity, retention, and code quality."),

                        html.H6("Why It Matters", className="mt-3"),
                        html.Ul([
                            html.Li("High developer satisfaction correlates with better retention rates"),
                            html.Li("Satisfied developers tend to produce higher quality code"),
                            html.Li("Teams with high satisfaction are more likely to innovate and experiment"),
                            html.Li("Developer satisfaction directly impacts team culture and collaboration"),
                        ]),

                        html.H6("How to Improve", className="mt-3"),
                        html.Ul([
                            html.Li("Provide comprehensive training on AI tools and features"),
                            html.Li("Create clear guidelines for AI tool usage"),
                            html.Li("Establish feedback loops for AI tool improvements"),
                            html.Li("Recognize and reward effective AI adoption"),
                            html.Li("Balance automation with creative work"),
                            html.Li("Address privacy and ethical concerns transparently"),
                        ]),
                    ])
                ),
            ]),

            dbc.Tab(label="Breakdown", tab_id="breakdown", children=[
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Satisfaction by Category", className="section-header"),
                        html.P("Breakdown of satisfaction scores across different aspects",
                               className="subsection-header"),
                        dcc.Graph(
                            figure=px.bar(
                                satisfaction_categories,
                                x='Category',
                                y='Score',
                                title='Satisfaction by Category (%)'
                            ).update_layout(height=400)
                        )
                    ])
                ),
            ]),

            dbc.Tab(label="Survey Data", tab_id="data"),
        ], id="satisfaction-tabs", active_tab="overview"),
    ])


def create_agile_velocity_layout():
    return html.Div([
        html.H1("Velocity", className="main-header mb-2"),
        html.P("Measuring the amount of work completed in each sprint", className="text-muted mb-4"),

        dbc.Row([
            dbc.Col(create_metric_card("Current Velocity", "48 points", "+9% from last sprint", "📈"), width=4),
            dbc.Col(create_metric_card("AI-Assisted Work", "83%", "+8% from last sprint", "📈"), width=4),
            dbc.Col(create_metric_card("Predictability", "100%", "+2% from last sprint", "📈"), width=4),
        ], className="mb-4"),

        dbc.Tabs([
            dbc.Tab(label="Overview", tab_id="overview", children=[
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Velocity Trends", className="section-header"),
                        html.P("Planned vs. completed story points over time", className="subsection-header"),
                        dcc.Graph(
                            figure=px.bar(
                                velocity_data,
                                x='Sprint',
                                y=['Planned', 'Completed', 'AI-Assisted'],
                                title='Velocity Trends (Story Points)',
                                barmode='group'
                            ).update_layout(height=400)
                        )
                    ])
                ),

                dbc.Card(
                    dbc.CardBody([
                        html.H5("Understanding Velocity", className="section-header"),
                        html.P("What this metric means and how to improve it", className="subsection-header"),

                        html.H6("What is Velocity?", className="mt-3"),
                        html.P(
                            "Velocity measures the amount of work a team completes during a sprint. It's typically measured in story points or other relative units of effort. Velocity helps teams predict how much work they can complete in future sprints and is a key metric for sprint planning."),

                        html.H6("Key Components", className="mt-3"),
                        html.Ul([
                            html.Li([html.Span("Planned Points:", className="fw-medium"),
                                     " The number of story points the team commits to completing in a sprint"]),
                            html.Li([html.Span("Completed Points:", className="fw-medium"),
                                     " The number of story points actually completed by the end of the sprint"]),
                            html.Li([html.Span("AI-Assisted Points:", className="fw-medium"),
                                     " Story points completed with AI assistance"]),
                            html.Li([html.Span("Predictability:", className="fw-medium"),
                                     " The ratio of completed to planned points, indicating how accurately the team estimates"]),
                        ]),

                        html.H6("AI's Impact on Velocity", className="mt-3"),
                        html.Ul([
                            html.Li("AI tools can significantly increase development velocity"),
                            html.Li("Teams may need to recalibrate story point estimates when using AI"),
                            html.Li("AI can help reduce variance in velocity by making work more predictable"),
                            html.Li(
                                "Tracking AI-assisted work separately helps understand the true impact of AI on productivity"),
                            html.Li(
                                "As AI adoption increases, teams should expect velocity to increase and then stabilize at a new baseline"),
                        ]),
                    ])
                ),
            ]),

            dbc.Tab(label="By Team", tab_id="by-team", children=[
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Velocity by Team", className="section-header"),
                        html.P("Comparing velocity, AI adoption, and predictability across teams",
                               className="subsection-header"),
                        dcc.Graph(
                            figure=px.bar(
                                velocity_by_team,
                                x='Team',
                                y=['Velocity', 'AI Percentage', 'Predictability'],
                                title='Velocity by Team',
                                barmode='group'
                            ).update_layout(height=400)
                        )
                    ])
                ),
            ]),

            dbc.Tab(label="Sprint Data", tab_id="data"),
        ], id="velocity-tabs", active_tab="overview"),
    ])


# Define the main layout with URL routing
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='theme-store', data={'theme': 'light'}),
    html.Div(id='page-content', className='content')
], id='main-container')


# Callback to update the page content based on URL
@callback(
    Output('page-content', 'children'),
    Output('main-container', 'className'),
    Input('url', 'pathname'),
    Input('theme-store', 'data')
)
def display_page(pathname, theme_data):
    theme_class = 'dark-theme' if theme_data.get('theme') == 'dark' else ''

    # Always include the sidebar
    content = [sidebar]

    if pathname == '/' or pathname == '':
        content.append(dashboard_layout)
    elif pathname == '/dora/deployment-frequency':
        content.append(create_dora_deployment_frequency_layout())
    elif pathname == '/space/satisfaction':
        content.append(create_space_satisfaction_layout())
    elif pathname == '/agile/velocity':
        content.append(create_agile_velocity_layout())
    else:
        # For other pages, we could implement them similarly or show a placeholder
        content.append(html.Div([
            html.H1(f"Page: {pathname}", className="main-header"),
            html.P("This page is under construction.", className="text-muted"),
            dbc.Button("Go to Dashboard", href="/", color="primary")
        ]))

    return content, theme_class


# Callback for theme toggle
@callback(
    Output('theme-store', 'data'),
    Output('theme-toggle', 'children'),
    Input('theme-toggle', 'n_clicks'),
    State('theme-store', 'data')
)
def toggle_theme(n_clicks, theme_data):
    if n_clicks is None:
        return theme_data, '🌙' if theme_data.get('theme') == 'light' else '☀️'

    current_theme = theme_data.get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    new_icon = '☀️' if new_theme == 'dark' else '🌙'

    return {'theme': new_theme}, new_icon


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
