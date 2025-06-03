# app/components/team_filter.py
from dash import dcc

def team_filter(team_list, id="team-selector"):
    return dcc.Dropdown(
        id=id,
        options=[{"label": t, "value": t} for t in sorted(team_list)],
        value=sorted(team_list),
        multi=True,
        placeholder="Filter by team"
    )