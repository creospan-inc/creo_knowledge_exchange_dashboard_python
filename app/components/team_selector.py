from dash import dcc

def team_selector_dropdown(dropdown_id, team_ids, placeholder="Select teams to display"):
    """
    Returns a reusable team selector dropdown component.
    :param dropdown_id: The id for the dropdown (str)
    :param team_ids: List of team ids (list of str)
    :param placeholder: Placeholder text (str)
    """
    return dcc.Dropdown(
        id=dropdown_id,
        options=[{'label': team, 'value': team} for team in team_ids],
        value=team_ids,
        multi=True,
        placeholder=placeholder
    )
