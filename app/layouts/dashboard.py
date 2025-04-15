from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

from ..components.helpers import create_metric_card
from ..data.metrics_data import (
    get_metrics_data,
    get_failure_rate_data,
    get_restore_time_data,
    get_satisfaction_data,
    get_performance_data,
    get_activity_data,
    get_communication_data,
    get_efficiency_data,
    get_efficiency_trend_data,
    get_velocity_data,
    get_cycle_time_data,
    get_sprint_burndown_data,
    get_ai_adoption_by_team,
    get_activity_trend_data
)

dashboard_layout = html.Div([
    html.H1("AI Adoption Metrics Dashboard", className="main-header mb-2"),
    html.P("Track your team's progress and efficiencies in adopting AI", className="text-muted mb-4"),

    dbc.Tabs(id="dashboard-tabs", active_tab="overview", children=[
        dbc.Tab(label="Overview", tab_id="overview"),
        dbc.Tab(label="DORA Metrics", tab_id="dora"),
        dbc.Tab(label="SPACE Metrics", tab_id="space"),
        dbc.Tab(label="Agile Metrics", tab_id="agile"),
    ]),
    html.Div(id="dashboard-tab-content", className="mt-4")
])

@callback(
    Output('dashboard-tab-content', 'children'),
    Input('dashboard-tabs', 'active_tab')
)
def render_dashboard_tab(tab):
    if tab == "overview":
        return create_dashboard_overview()
    elif tab == "dora":
        return create_dashboard_dora()
    elif tab == "space":
        return create_dashboard_space()
    elif tab == "agile":
        return create_dashboard_agile()
    return html.Div("Select a tab to view dashboard data.")

def create_dashboard_overview():
    return html.Div([
        dbc.Row([
            dbc.Col(create_metric_card("Deployment Frequency", "4.2/week", "+20.1%", "🔄"), width=3),
            dbc.Col(create_metric_card("Lead Time", "3.5 days", "-15.2%", "⏱️"), width=3),
            dbc.Col(create_metric_card("Satisfaction", "85%", "+5%", "👥"), width=3),
            dbc.Col(create_metric_card("AI Adoption", "68%", "+12.3%", "🤖"), width=3),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.H5("Metrics Overview", className="section-header"),
                dcc.Graph(figure=px.line(get_metrics_data(), x="month",
                    y=["Deployment Frequency", "Lead Time", "Team Satisfaction", "AI Adoption"]).update_layout(
                    title="Metric Trends", height=400))
            ], width=8),

            dbc.Col([
                html.H5("Team Efficiency", className="section-header"),
                html.P("AI-assisted vs traditional tasks"),
                dcc.Graph(figure=go.Figure(data=[
                    go.Bar(name='Traditional', x=get_efficiency_data()['Task'], y=get_efficiency_data()['Traditional']),
                    go.Bar(name='AI-Assisted', x=get_efficiency_data()['Task'], y=get_efficiency_data()['AI-Assisted']),
                ]).update_layout(title="Time on Tasks (Minutes)", barmode="group", height=400))
            ], width=4),
        ], className="mb-4"),

        html.H5("Recent Activity", className="section-header"),
        dbc.ListGroup([
            dbc.ListGroupItem([
                dbc.Row([
                    dbc.Col(html.Img(src=f"https://via.placeholder.com/40x40.png?text={activity['user'][0:2]}", width=40), width=1),
                    dbc.Col([
                        html.Div(activity["user"], className="fw-bold"),
                        html.Div(activity["description"]),
                        html.Small(activity["time"], className="text-muted")
                    ])
                ])
            ]) for activity in get_activity_data().to_dict("records")
        ])
    ])

def create_dashboard_dora():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H5("Deployment Frequency", className="section-header"),
                dcc.Graph(
                    figure=px.bar(
                        get_metrics_data(),
                        x='month',
                        y='Deployment Frequency',
                        title='Deployments Per Week'
                    ).update_layout(height=350)
                )
            ], width=6),

            dbc.Col([
                html.H5("Lead Time for Changes", className="section-header"),
                dcc.Graph(
                    figure=px.line(
                        get_metrics_data(),
                        x='month',
                        y='Lead Time',
                        title='Lead Time (Days)'
                    ).update_layout(height=350)
                )
            ], width=6),
        ]),

        dbc.Row([
            dbc.Col([
                html.H5("Change Failure Rate", className="section-header"),
                dcc.Graph(
                    figure=px.bar(
                        get_failure_rate_data(),
                        x='Month',
                        y='Failure Rate',
                        title='Failure Rate (%)'
                    ).update_layout(height=350)
                )
            ], width=6),

            dbc.Col([
                html.H5("Time to Restore", className="section-header"),
                dcc.Graph(
                    figure=px.line(
                        get_restore_time_data(),
                        x='Month',
                        y='Restore Time',
                        title='Time to Restore (Hours)'
                    ).update_layout(height=350)
                )
            ], width=6),
        ])
    ])

def create_dashboard_space():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H5("Satisfaction"),
                dcc.Graph(figure=px.bar(
                    get_satisfaction_data(),
                    x="Month", y="Score",
                    title="Satisfaction (%)"
                ).update_layout(height=300))
            ], width=4),

            dbc.Col([
                html.H5("Performance"),
                dcc.Graph(figure=px.line(
                    get_performance_data(),
                    x="Month", y="Quality",
                    title="Quality (%)"
                ).update_layout(height=300))
            ], width=4),

            dbc.Col([
                html.H5("Activity"),
                dcc.Graph(figure=px.bar(
                    get_activity_trend_data(),
                    x="Month", y="Prompts",
                    title="AI Prompts"
                ).update_layout(height=300))
            ], width=4)
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.H5("Communication"),
                dcc.Graph(figure=px.line(
                    get_communication_data(),
                    x="Month", y="Collaboration",
                    title="Collaboration"
                ).update_layout(height=300))
            ], width=6),

            dbc.Col([
                html.H5("Efficiency"),
                dcc.Graph(figure=px.bar(
                    get_efficiency_trend_data(),
                    x="Month", y="Time Saved",
                    title="Time Saved (Hours)"
                ).update_layout(height=300))
            ], width=6)
        ])
    ])

def create_dashboard_agile():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H5("Velocity"),
                dcc.Graph(figure=px.line(get_velocity_data(), x="Sprint", y="Velocity",
                    title="Velocity").update_layout(height=350))
            ], width=6),
            dbc.Col([
                html.H5("Cycle Time"),
                dcc.Graph(figure=px.bar(get_cycle_time_data(), x="Month", y="Cycle Time",
                    title="Cycle Time (Days)").update_layout(height=350))
            ], width=6)
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.H5("Sprint Burndown"),
                dcc.Graph(figure=px.line(get_sprint_burndown_data(), x="Day", y="Remaining",
                    title="Burndown").update_layout(height=350))
            ], width=6),
            dbc.Col([
                html.H5("AI Adoption by Team"),
                dcc.Graph(figure=px.bar(get_ai_adoption_by_team(), x="Team", y="Adoption",
                    title="AI Adoption (%)").update_layout(height=350))
            ], width=6)
        ])
    ])
