import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html

def bathrooms_layout():
    return dmc.Stack(
        [
            dmc.Title("Bathrooms", order=2),
        ],
        gap="md",
    )
