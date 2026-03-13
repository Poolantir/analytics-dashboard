import dash_mantine_components as dmc
from dash_iconify import DashIconify


def settings_layout():
    profile_section = dmc.Card(
        dmc.Stack(
            [
                dmc.Text("Profile", fw=600, size="lg"),
                dmc.Divider(),
                dmc.TextInput(
                    label="Display Name",
                    placeholder="Your name",
                    value="",
                ),
                dmc.TextInput(
                    label="Email",
                    placeholder="you@example.com",
                    value="",
                ),
            ],
            gap="sm",
        ),
        withBorder=True,
    )

    notification_section = dmc.Card(
        dmc.Stack(
            [
                dmc.Text("Notifications", fw=600, size="lg"),
                dmc.Divider(),
                dmc.Switch(
                    label="Email alerts",
                    checked=True,
                ),
                dmc.Switch(
                    label="Push notifications",
                    checked=False,
                ),
                dmc.Switch(
                    label="Weekly digest",
                    checked=True,
                ),
            ],
            gap="sm",
        ),
        withBorder=True,
    )

    preferences_section = dmc.Card(
        dmc.Stack(
            [
                dmc.Text("Preferences", fw=600, size="lg"),
                dmc.Divider(),
                dmc.Select(
                    label="Temperature Unit",
                    data=[
                        {"value": "C", "label": "Celsius (°C)"},
                        {"value": "F", "label": "Fahrenheit (°F)"},
                    ],
                    value="F",
                    w=200,
                ),
                dmc.Select(
                    label="Theme",
                    data=[
                        {"value": "light", "label": "Light"},
                        {"value": "dark", "label": "Dark"},
                        {"value": "system", "label": "System"},
                    ],
                    value="light",
                    w=200,
                ),
            ],
            gap="sm",
        ),
        withBorder=True,
    )

    logout_section = dmc.Card(
        dmc.Group(
            [
                dmc.Stack(
                    [
                        dmc.Text("Session", fw=600, size="lg"),
                        dmc.Text(
                            "Sign out of your Poolantir account",
                            c="dimmed",
                            size="sm",
                        ),
                    ],
                    gap=4,
                ),
                dmc.Button(
                    "Log out",
                    leftSection=DashIconify(icon="mdi:logout", width=18),
                    color="red",
                    variant="outline",
                ),
            ],
            justify="space-between",
            align="center",
        ),
        withBorder=True,
    )

    return dmc.Stack(
        [
            dmc.Title("Settings", order=2),
            dmc.Text("Manage your account and preferences", c="dimmed", size="sm"),
            profile_section,
            notification_section,
            preferences_section,
            logout_section,
        ],
        gap="md",
        maw=600,
    )
