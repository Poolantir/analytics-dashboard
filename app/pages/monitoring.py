import dash_mantine_components as dmc
from dash_iconify import DashIconify


def monitoring_layout():
    return dmc.Stack(
        [
            dmc.Title("Monitoring", order=2),
        ],
        gap="md",
    )