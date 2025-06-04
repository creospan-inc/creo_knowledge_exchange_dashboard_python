from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash.exceptions
import plotly.express as px

from .components.sidebar import sidebar
from .layouts.dashboard import dashboard_layout

# DORA Metrics
from .layouts.dora import deployment_frequency
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

from app.data.metrics_data import get_failure_rate_data, get_lead_time_data, get_restore_time_data, get_velocity_data, get_cycle_time_data, get_sprint_burndown_data, get_activity_trend_data, get_efficiency_trend_data, get_satisfaction_data, get_performance_data, get_communication_data

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
    # Page routing and theme toggle
    @app.callback(
        Output('page-content', 'children'),
        Output('main-container', 'className'),
        Input('url', 'pathname'),
        Input('theme-store', 'data')
    )
    def display_page(pathname, theme_data):
        theme_class = 'dark-theme' if theme_data and theme_data.get('theme') == 'dark' else 'light-theme'
        content = [sidebar]

        if pathname in ['/', '']:
            content.append(dashboard_layout)

        elif pathname == '/ai/time-saving-by-role':
            content.append(ai_time_saving_by_role_layout)

        elif pathname == '/dora/deployment-frequency':
            content.append(deployment_frequency.layout)
        elif pathname == '/dora/lead-time':
            content.append(dora_lead_time_layout)
        elif pathname == '/dora/change-failure-rate':
            content.append(dora_change_failure_rate_layout)
        elif pathname == '/dora/time-to-restore':
            content.append(dora_time_to_restore_layout)

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

        elif pathname == '/agile/velocity':
            content.append(agile_velocity_layout)
        elif pathname == '/agile/cycle-time':
            content.append(agile_cycle_time_layout)
        elif pathname == '/agile/sprint-burndown':
            content.append(agile_sprint_burndown_layout)
        elif pathname == '/agile/ai-adoption':
            content.append(agile_ai_adoption_layout)

        elif pathname == '/settings':
            content.append(settings_layout)

        else:
            content.append(html.Div([
                html.H1("Page Not Found", className="main-header"),
                html.P(f"No content found for {pathname}", className="text-muted"),
                html.A("Return to Dashboard", href="/", className="btn btn-primary mt-2")
            ]))

        return content, theme_class

    @app.callback(
        Output('theme-store', 'data'),
        Input('theme-toggle', 'n_clicks'),
        State('theme-store', 'data'),
        prevent_initial_call=True
    )
    def toggle_theme(n_clicks, current_theme_data):
        if n_clicks is None:
            raise dash.exceptions.PreventUpdate

        current_theme = current_theme_data.get('theme', 'light') if current_theme_data else 'light'
        new_theme = 'dark' if current_theme == 'light' else 'light'
        return {'theme': new_theme}

    @app.callback(
        Output('theme-toggle', 'children'),
        Input('theme-store', 'data'),
        prevent_initial_call=True
    )
    def update_toggle_icon(theme_data):
        return '☀️' if theme_data.get('theme') == 'dark' else '🌙'

    # --- NEW: Collapsible Sidebar Section Callbacks ---
    @app.callback(Output("collapse-nav", "is_open"),
                  Input("toggle-nav", "n_clicks"),
                  State("collapse-nav", "is_open"))
    def toggle_nav(n, is_open):
        return not is_open if n else is_open

    @app.callback(Output("collapse-ai", "is_open"),
                  Input("toggle-ai", "n_clicks"),
                  State("collapse-ai", "is_open"))
    def toggle_ai(n, is_open):
        return not is_open if n else is_open

    @app.callback(Output("collapse-dora", "is_open"),
                  Input("toggle-dora", "n_clicks"),
                  State("collapse-dora", "is_open"))
    def toggle_dora(n, is_open):
        return not is_open if n else is_open

    @app.callback(Output("collapse-space", "is_open"),
                  Input("toggle-space", "n_clicks"),
                  State("collapse-space", "is_open"))
    def toggle_space(n, is_open):
        return not is_open if n else is_open

    @app.callback(Output("collapse-agile", "is_open"),
                  Input("toggle-agile", "n_clicks"),
                  State("collapse-agile", "is_open"))
    def toggle_agile(n, is_open):
        return not is_open if n else is_open

    @app.callback(
        Output('deployment-frequency-graph', 'figure'),
        Input('team-selector', 'value')
    )
    def update_deployment_graph(selected_teams):
        print("CALLBACK TRIGGERED", selected_teams)
        df = deployment_frequency.get_deployment_frequency_data()
        print("DataFrame preview:\n", df.head())
        print("Columns:", df.columns)
        print("Selected teams:", selected_teams)
        if df.empty:
            print("⚠️ No data returned from get_deployment_frequency_data()")
            return px.bar(title="No Data Available")
        filtered_df = df[df['team_id'].astype(str).isin([str(t) for t in selected_teams])]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.bar(title="No Data for Selected Teams")
        return px.bar(
            filtered_df,
            x='Month',
            y='Frequency',
            color='team_id',
            barmode='group',
            title="Deployment Frequency by Team"
        )

    @app.callback(
        Output('failure-rate-graph', 'figure'),
        Input('failure-rate-team-selector', 'value')
    )
    def update_failure_rate_graph(selected_teams):
        print("FAILURE RATE CALLBACK TRIGGERED", selected_teams)
        df = get_failure_rate_data()
        print("Failure Rate DataFrame preview:\n", df.head())
        print("Columns:", df.columns)
        print("Selected teams:", selected_teams)
        if df.empty:
            print("⚠️ No data returned from get_failure_rate_data()")
            return px.bar(title="No Data Available")
        filtered_df = df[df['team_id'].astype(str).isin([str(t) for t in selected_teams])]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.bar(title="No Data for Selected Teams")
        return px.bar(
            filtered_df,
            x='Month',
            y='Failure Rate',
            color='team_id',
            barmode='group',
            title="Failure Rate by Team"
        )

    @app.callback(
        Output('lead-time-graph', 'figure'),
        Input('lead-time-team-selector', 'value')
    )
    def update_lead_time_graph(selected_teams):
        print("LEAD TIME CALLBACK TRIGGERED", selected_teams)
        df = get_lead_time_data()
        print("Lead Time DataFrame preview:\n", df.head())
        print("Columns:", df.columns)
        print("Selected teams:", selected_teams)
        if df.empty:
            print("⚠️ No data returned from get_lead_time_data()")
            return px.line(title="No Data Available")
        filtered_df = df[df['team_id'].astype(str).isin([str(t) for t in selected_teams])]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.line(title="No Data for Selected Teams")
        return px.line(
            filtered_df,
            x='Month',
            y='Lead Time',
            color='team_id',
            title="Lead Time by Team"
        )

    @app.callback(
        Output('restore-time-graph', 'figure'),
        Input('restore-time-team-selector', 'value')
    )
    def update_restore_time_graph(selected_teams):
        print("RESTORE TIME CALLBACK TRIGGERED", selected_teams)
        df = get_restore_time_data()
        print("Restore Time DataFrame preview:\n", df.head())
        print("Columns:", df.columns)
        print("Selected teams:", selected_teams)
        if df.empty:
            print("⚠️ No data returned from get_restore_time_data()")
            return px.line(title="No Data Available")
        filtered_df = df[df['team_id'].astype(str).isin([str(t) for t in selected_teams])]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.line(title="No Data for Selected Teams")
        return px.line(
            filtered_df,
            x='Month',
            y='Restore Time',
            color='team_id',
            title="Time to Restore Service by Team"
        )

    @app.callback(
        Output('velocity-graph', 'figure'),
        Input('velocity-team-selector', 'value')
    )
    def update_velocity_graph(selected_teams):
        print("VELOCITY CALLBACK TRIGGERED", selected_teams)
        df = get_velocity_data()
        print("Velocity DataFrame preview:\n", df.head())
        print("Columns:", df.columns)
        print("Selected teams:", selected_teams)
        if df.empty:
            print("⚠️ No data returned from get_velocity_data()")
            return px.bar(title="No Data Available")
        filtered_df = df[df['team_id'].astype(str).isin([str(t) for t in selected_teams])]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.bar(title="No Data for Selected Teams")
        return px.bar(
            filtered_df,
            x='Sprint',
            y='Velocity',
            color='team_id',
            barmode='group',
            title="Sprint Velocity by Team"
        )

    @app.callback(
        Output('cycle-time-graph', 'figure'),
        Input('cycle-time-team-selector', 'value')
    )
    def update_cycle_time_graph(selected_teams):
        print("CYCLE TIME CALLBACK TRIGGERED", selected_teams)
        df = get_cycle_time_data()
        print("Cycle Time DataFrame preview:\n", df.head())
        print("Columns:", df.columns)
        print("Selected teams:", selected_teams)
        if df.empty:
            print("⚠️ No data returned from get_cycle_time_data()")
            return px.line(title="No Data Available")
        filtered_df = df[df['team_id'].astype(str).isin([str(t) for t in selected_teams])]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.line(title="No Data for Selected Teams")
        return px.line(
            filtered_df,
            x='Month',
            y='Cycle Time',
            color='team_id',
            title="Cycle Time Trend by Team"
        )

    @app.callback(
        Output('sprint-burndown-graph', 'figure'),
        Input('sprint-burndown-team-selector', 'value')
    )
    def update_sprint_burndown_graph(selected_teams):
        print("SPRINT BURNDOWN CALLBACK TRIGGERED", selected_teams)
        df = get_sprint_burndown_data()
        print("Sprint Burndown DataFrame preview:\n", df.head())
        print("Columns:", df.columns)
        print("Selected teams:", selected_teams)
        if df.empty:
            print("⚠️ No data returned from get_sprint_burndown_data()")
            return px.line(title="No Data Available")
        filtered_df = df[df['team_id'].astype(str).isin([str(t) for t in selected_teams])]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.line(title="No Data for Selected Teams")
        return px.line(
            filtered_df,
            x='Day',
            y='Remaining',
            color='team_id',
            title="Sprint Burndown by Team"
        )

    @app.callback(
        Output('activity-graph', 'figure'),
        Input('activity-team-selector', 'value')
    )
    def update_activity_graph(selected_teams):
        print("ACTIVITY CALLBACK TRIGGERED", selected_teams)
        df = get_activity_trend_data()
        print("Activity DataFrame preview:\n", df.head())
        print("Columns:", df.columns)
        print("Selected teams:", selected_teams)
        if df.empty or 'team_id' not in df.columns:
            print("⚠️ No data returned from get_activity_trend_data() or missing 'team_id'")
            return px.line(title="No Data Available")
        filtered_df = df[df['team_id'].astype(str).isin([str(t) for t in selected_teams])]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.line(title="No Data for Selected Teams")
        return px.line(
            filtered_df,
            x='Month',
            y=['Prompts', 'Commits'],
            color='team_id',
            title="Developer Activity Trends by Team"
        )

    @app.callback(
        Output('efficiency-graph', 'figure'),
        Input('efficiency-team-selector', 'value')
    )
    def update_efficiency_graph(selected_teams):
        print("EFFICIENCY CALLBACK TRIGGERED", selected_teams)
        df = get_efficiency_trend_data()
        print("Efficiency DataFrame preview:\n", df.head())
        print("Unique team_ids in df:", df['team_id'].unique() if 'team_id' in df.columns else "No team_id column")
        print("Selected teams:", selected_teams)
        if df.empty or 'team_id' not in df.columns:
            print("⚠️ No data returned from get_efficiency_trend_data() or missing 'team_id'")
            return px.line(title="No Data Available")
        df['team_id'] = df['team_id'].astype(str).str.strip()
        selected_teams = [str(t).strip() for t in selected_teams]
        filtered_df = df[df['team_id'].isin(selected_teams)]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.line(title="No Data for Selected Teams")
        return px.line(
            filtered_df,
            x='Month',
            y=['Time Saved', 'Productive Hours'],
            color='team_id',
            title="Efficiency Over Time by Team"
        )

    @app.callback(
        Output('satisfaction-graph', 'figure'),
        Input('satisfaction-team-selector', 'value')
    )
    def update_satisfaction_graph(selected_teams):
        print("SATISFACTION CALLBACK TRIGGERED", selected_teams)
        df = get_satisfaction_data()
        print("Satisfaction DataFrame preview:\n", df.head())
        print("Unique team_ids in df:", df['team_id'].unique() if 'team_id' in df.columns else "No team_id column")
        print("Selected teams:", selected_teams)
        if df.empty or 'team_id' not in df.columns:
            print("⚠️ No data returned from get_satisfaction_data() or missing 'team_id'")
            return px.line(title="No Data Available")
        df['team_id'] = df['team_id'].astype(str).str.strip()
        selected_teams = [str(t).strip() for t in selected_teams]
        filtered_df = df[df['team_id'].isin(selected_teams)]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.line(title="No Data for Selected Teams")
        return px.line(
            filtered_df,
            x='Month',
            y='Score',
            color='team_id',
            title="Satisfaction Over Time by Team"
        )

    @app.callback(
        Output('performance-graph', 'figure'),
        Input('performance-team-selector', 'value')
    )
    def update_performance_graph(selected_teams):
        print("PERFORMANCE CALLBACK TRIGGERED", selected_teams)
        df = get_performance_data()
        print("Performance DataFrame preview:\n", df.head())
        print("Unique team_ids in df:", df['team_id'].unique() if 'team_id' in df.columns else "No team_id column")
        print("Selected teams:", selected_teams)
        if df.empty or 'team_id' not in df.columns:
            print("⚠️ No data returned from get_performance_data() or missing 'team_id'")
            return px.line(title="No Data Available")
        df['team_id'] = df['team_id'].astype(str).str.strip()
        selected_teams = [str(t).strip() for t in selected_teams]
        filtered_df = df[df['team_id'].isin(selected_teams)]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.line(title="No Data for Selected Teams")
        return px.line(
            filtered_df,
            x='Month',
            y=['Quality', 'Impact'],
            color='team_id',
            title="Performance Over Time by Team"
        )

    @app.callback(
        Output('communication-graph', 'figure'),
        Input('communication-team-selector', 'value')
    )
    def update_communication_graph(selected_teams):
        print("COMMUNICATION CALLBACK TRIGGERED", selected_teams)
        df = get_communication_data()
        print("Communication DataFrame preview:\n", df.head())
        print("Unique team_ids in df:", df['team_id'].unique() if 'team_id' in df.columns else "No team_id column")
        print("Selected teams:", selected_teams)
        if df.empty or 'team_id' not in df.columns:
            print("⚠️ No data returned from get_communication_data() or missing 'team_id'")
            return px.line(title="No Data Available")
        df['team_id'] = df['team_id'].astype(str).str.strip()
        selected_teams = [str(t).strip() for t in selected_teams]
        filtered_df = df[df['team_id'].isin(selected_teams)]
        print("Filtered DataFrame:\n", filtered_df)
        if filtered_df.empty:
            print("⚠️ No data for selected teams:", selected_teams)
            return px.line(title="No Data for Selected Teams")
        return px.line(
            filtered_df,
            x='Month',
            y='Collaboration',
            color='team_id',
            title="Collaboration Over Time by Team"
        )