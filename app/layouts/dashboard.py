
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from app.data.metrics_data import (
    metrics_data,
    failure_rate_data,
    restore_time_data,
    satisfaction_data,
    performance_data,
    activity_trend_data,
    communication_data,
    efficiency_trend_data,
    velocity_data,
    cycle_time_data,
    sprint_burndown_data,
    ai_adoption_by_team,
    activity_data
)

# Dashboard layout with tab container
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

# Callback to update tab content
@callback(
    Output("dashboard-tab-content", "children"),
    Input("dashboard-tabs", "active_tab")
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


def create_metric_card(title, value, delta, icon):
    delta_class = "metric-delta-up" if '+' in delta else "metric-delta-down"
    return dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(html.Div(title, className="fw-medium"), width=10),
                dbc.Col(html.Div(icon), width=2),
            ]),
            html.Div(value, className="metric-value mt-2"),
            html.Div(delta, className=f"metric-delta {delta_class}"),
        ]),
        className="card h-100"
    )

def create_dashboard_overview():
    return html.Div([
        dbc.Row([
            dbc.Col(create_metric_card("Deployment Frequency", "4.2/week", "+20.1%", "🔄"), width=3),
            dbc.Col(create_metric_card("Lead Time", "3.5 days", "-15.2%", "⏱️"), width=3),
            dbc.Col(create_metric_card("Satisfaction", "85%", "+5%", "😊"), width=3),
            dbc.Col(create_metric_card("AI Adoption", "68%", "+12.3%", "🤖"), width=3),
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.H5("Metrics Overview"),
                dcc.Graph(
                    figure=px.line(
                        metrics_data,
                        x='month',
                        y=['Deployment Frequency', 'Lead Time', 'Team Satisfaction', 'AI Adoption'],
                        title='Key Metrics Over Time'
                    ).update_layout(height=400)
                )
            ], width=8),

            dbc.Col([
                html.H5("Recent Activity"),
                dbc.ListGroup([
                    dbc.ListGroupItem([
                        dbc.Row([
                            dbc.Col(
                                html.Div(activity['user'][0:2], className="avatar text-center"), width=2
                            ),
                            dbc.Col([
                                html.Div(activity['user'], className="fw-bold"),
                                html.Div(activity['description']),
                                html.Small(activity['time'], className="text-muted")
                            ], width=10)
                        ])
                    ]) for activity in activity_data.to_dict('records')
                ])
            ], width=4),
        ])
    ])

def create_dashboard_dora():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H5("Deployment Frequency"),
                dcc.Graph(
                    figure=px.bar(metrics_data, x="month", y="Deployment Frequency").update_layout(height=350)
                )
            ], width=6),
            dbc.Col([
                html.H5("Lead Time for Changes"),
                dcc.Graph(
                    figure=px.line(metrics_data, x="month", y="Lead Time").update_layout(height=350)
                )
            ], width=6),
        ]),
        dbc.Row([
            dbc.Col([
                html.H5("Change Failure Rate"),
                dcc.Graph(
                    figure=px.bar(failure_rate_data, x="Month", y="Rate").update_layout(height=350)
                )
            ], width=6),
            dbc.Col([
                html.H5("Time to Restore Service"),
                dcc.Graph(
                    figure=px.line(restore_time_data, x="Month", y="Hours").update_layout(height=350)
                )
            ], width=6),
        ])
    ])

def create_dashboard_space():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H5("Satisfaction"),
                dcc.Graph(
                    figure=px.bar(satisfaction_data, x="Month", y="Score", title="Satisfaction (%)").update_layout(height=300)
                )
            ], width=4),
            dbc.Col([
                html.H5("Performance"),
                dcc.Graph(
                    figure=px.line(performance_data, x="Month", y="Quality Score", title="Quality (%)").update_layout(height=300)
                )
            ], width=4),
            dbc.Col([
                html.H5("Activity"),
                dcc.Graph(
                    figure=px.bar(activity_trend_data, x="Month", y="Prompts", title="AI Prompts").update_layout(height=300)
                )
            ], width=4)
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.H5("Communication"),
                dcc.Graph(
                    figure=px.line(communication_data, x="Month", y="Collaboration Index", title="Collaboration").update_layout(height=300)
                )
            ], width=6),
            dbc.Col([
                html.H5("Efficiency"),
                dcc.Graph(
                    figure=px.bar(efficiency_trend_data, x="Month", y="Time Saved", title="Time Saved (Hours)").update_layout(height=300)
                )
            ], width=6)
        ])
    ])

def create_dashboard_agile():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H5("Velocity"),
                dcc.Graph(
                    figure=px.line(velocity_data, x="Sprint", y="Completed", title="Velocity").update_layout(height=350)
                )
            ], width=6),
            dbc.Col([
                html.H5("Cycle Time"),
                dcc.Graph(
                    figure=px.bar(cycle_time_data, x="Month", y="AI-Assisted", title="Cycle Time (AI-Assisted)").update_layout(height=350)
                )
            ], width=6),
        ]),

        dbc.Row([
            dbc.Col([
                html.H5("Sprint Burndown"),
                dcc.Graph(
                    figure=px.line(sprint_burndown_data, x="Day", y="Remaining", title="Sprint Burndown").update_layout(height=350)
                )
            ], width=6),

            dbc.Col([
                html.H5("AI Adoption by Team"),
                dcc.Graph(
                    figure=px.bar(ai_adoption_by_team, x="Team", y="Adoption", title="AI Adoption").update_layout(height=350)
                )
            ], width=6),
        ])
    ])
