import dash_mantine_components as dmc
from dash_iconify import DashIconify

def settings_layout():
    return dmc.Stack(
        [
            dmc.Title("Settings", order=2),
        ],
        gap="md",
    )
