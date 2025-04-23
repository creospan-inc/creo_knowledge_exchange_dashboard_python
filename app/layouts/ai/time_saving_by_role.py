from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

from ...data.metrics_data import get_time_saving_by_role, get_time_saving_by_role_trend

layout = html.Div([
    html.H1("Time Saving by Role", className="main-header mb-3"),
    html.P("Analyze how AI tools impact time savings across different roles in your organization", className="text-muted mb-4"),

    dbc.Row([
        dbc.Col([
            html.Div([
                html.H3("Monthly Average", className="card-title h5"),
                html.P("Average hours saved per month per role", className="card-text text-muted"),
                dcc.Graph(
                    figure=px.bar(
                        get_time_saving_by_role(), 
                        x='Role', 
                        y='Hours Saved', 
                        color='Role',
                        title="Average Hours Saved by Role (Monthly)"
                    ).update_layout(height=400)
                )
            ], className="border rounded p-3 h-100")
        ], width=6),

        dbc.Col([
            html.Div([
                html.H3("Percentage of Work Time", className="card-title h5"),
                html.P("AI-assisted vs traditional work percentage", className="card-text text-muted"),
                dcc.Graph(
                    figure=px.pie(
                        get_time_saving_by_role(),
                        values='Percent Time Saved', 
                        names='Role', 
                        title="Percentage of Time Saved by Role"
                    ).update_layout(height=400)
                )
            ], className="border rounded p-3 h-100")
        ], width=6)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            html.Div([
                html.H3("Trend Analysis", className="card-title h5"),
                html.P("How time savings have evolved over time by role", className="card-text text-muted"),
                dcc.Graph(
                    figure=px.line(
                        get_time_saving_by_role_trend(), 
                        x='Month', 
                        y=['Product Manager', 'Designer', 'Engineer', 'QA'],
                        title="Time Saving Trend by Role (Hours)"
                    ).update_layout(height=400)
                )
            ], className="border rounded p-3")
        ], width=12)
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            html.Div([
                html.H3("Comparative Analysis", className="card-title h5"),
                html.P("Comparison between different roles", className="card-text text-muted"),
                html.Div([
                    html.Div([
                        html.H4("Product Manager", className="h5"),
                        html.P("15.3 hours saved monthly", className="h2 text-primary mb-0"),
                        html.P("Primarily from automation of user story generation and requirement analysis", className="text-muted")
                    ], className="py-2 border-bottom"),
                    
                    html.Div([
                        html.H4("Designer", className="h5"),
                        html.P("12.8 hours saved monthly", className="h2 text-primary mb-0"),
                        html.P("Time saved through automated asset generation and UI pattern suggestions", className="text-muted")
                    ], className="py-2 border-bottom"),
                    
                    html.Div([
                        html.H4("Engineer", className="h5"),
                        html.P("20.5 hours saved monthly", className="h2 text-primary mb-0"),
                        html.P("Major savings from code generation, refactoring, and debugging assistance", className="text-muted")
                    ], className="py-2 border-bottom"),
                    
                    html.Div([
                        html.H4("QA", className="h5"),
                        html.P("18.2 hours saved monthly", className="h2 text-primary mb-0"),
                        html.P("Improvements from test script generation and automated test analysis", className="text-muted")
                    ], className="py-2")
                ])
            ], className="border rounded p-3")
        ], width=12)
    ])
]) 