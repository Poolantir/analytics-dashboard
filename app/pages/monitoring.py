import dash_mantine_components as dmc
from dash_iconify import DashIconify


def monitoring_layout():
    def ghost_card(title, icon, h="160px"):
        return dmc.Card(
            dmc.Stack(
                [
                    DashIconify(icon=icon, width=28, color="dimmed"),
                    dmc.Text(title, size="sm", fw=500, c="dimmed"),
                    dmc.Skeleton(h=8, w="80%", radius="xl"),
                    dmc.Skeleton(h=8, w="60%", radius="xl"),
                ],
                gap="xs",
                align="center",
                justify="center",
                h="100%",
            ),
            withBorder=True,
            h=h,
            style={"minWidth": 0},
        )

    return dmc.Stack(
        [
            dmc.Title("Monitoring", order=2),
            dmc.Text(
                "Real-time pool analytics overview",
                c="dimmed",
                size="sm",
            ),
            dmc.SimpleGrid(
                [
                    ghost_card("Water Temperature", "mdi:thermometer-water", h="180px"),
                    ghost_card("pH Level", "mdi:flask-outline", h="180px"),
                    ghost_card("Chlorine", "mdi:water-opacity", h="180px"),
                    ghost_card("Filter Pressure", "mdi:gauge", h="180px"),
                ],
                cols={"base": 1, "xs": 2, "md": 4},
                spacing="md",
            ),
            dmc.SimpleGrid(
                [
                    ghost_card("Temperature History", "mdi:chart-line", h="260px"),
                    ghost_card("Chemical Balance", "mdi:chart-bar", h="260px"),
                ],
                cols={"base": 1, "md": 2},
                spacing="md",
            ),
            dmc.SimpleGrid(
                [
                    ghost_card("Alerts & Notifications", "mdi:bell-outline", h="200px"),
                    ghost_card("Equipment Status", "mdi:cog-outline", h="200px"),
                    ghost_card("Energy Usage", "mdi:lightning-bolt-outline", h="200px"),
                ],
                cols={"base": 1, "sm": 3},
                spacing="md",
            ),
        ],
        gap="md",
    )
