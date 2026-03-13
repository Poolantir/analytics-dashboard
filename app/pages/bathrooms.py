import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html


BUILDINGS = [
    {"value": "seamans", "label": "Seamans Center"},
    {"value": "main_library", "label": "Main Library"},
    {"value": "pappajohn", "label": "Pappajohn Business Building"},
]

FLOORS = [
    {"value": "1", "label": "Floor 1"},
    {"value": "2", "label": "Floor 2"},
    {"value": "3", "label": "Floor 3"},
]

TOILETS = [
    {"id": "toilet-1", "label": "Restroom A", "x": "18%", "y": "30%", "status": "available"},
    {"id": "toilet-2", "label": "Restroom B", "x": "50%", "y": "55%", "status": "occupied"},
    {"id": "toilet-3", "label": "Restroom C", "x": "75%", "y": "25%", "status": "available"},
    {"id": "toilet-4", "label": "Restroom D", "x": "60%", "y": "78%", "status": "maintenance"},
]

STATUS_COLORS = {
    "available": "green",
    "occupied": "red",
    "maintenance": "yellow",
}


def _toilet_marker(toilet):
    color = STATUS_COLORS.get(toilet["status"], "gray")
    return dmc.Tooltip(
        label=f"{toilet['label']} — {toilet['status']}",
        children=dmc.ActionIcon(
            DashIconify(icon="mdi:toilet", width=22),
            color=color,
            variant="filled",
            size="lg",
            radius="xl",
        ),
        position="top",
        withArrow=True,
        style={
            "position": "absolute",
            "left": toilet["x"],
            "top": toilet["y"],
        },
    )


def _floor_plan():
    markers = [_toilet_marker(t) for t in TOILETS]

    plan = html.Div(
        [
            dmc.Skeleton(h="100%", w="100%", radius="sm", visible=True),
            *markers,
        ],
        style={
            "position": "relative",
            "width": "100%",
            "height": "400px",
            "borderRadius": "var(--mantine-radius-sm)",
            "overflow": "hidden",
        },
    )
    return plan


def _map_placeholder():
    return dmc.Card(
        dmc.Stack(
            [
                DashIconify(icon="mdi:map-marker-radius-outline", width=36, color="dimmed"),
                dmc.Text("Campus map will load here", c="dimmed", size="sm"),
                dmc.Skeleton(h=200, radius="sm"),
            ],
            align="center",
            gap="sm",
        ),
        withBorder=True,
    )


def bathrooms_layout():
    filters = dmc.Group(
        [
            dmc.Select(
                label="Building",
                placeholder="Select a building",
                data=BUILDINGS,
                w=250,
                value="seamans",
            ),
            dmc.Select(
                label="Floor",
                placeholder="Select a floor",
                data=FLOORS,
                w=150,
                value="1",
            ),
        ],
        align="end",
    )

    legend = dmc.Group(
        [
            dmc.Badge("Available", color="green", variant="dot"),
            dmc.Badge("Occupied", color="red", variant="dot"),
            dmc.Badge("Maintenance", color="yellow", variant="dot"),
        ],
        gap="lg",
    )

    return dmc.Stack(
        [
            dmc.Title("Bathrooms", order=2),
            dmc.Text(
                "Building restroom availability at a glance",
                c="dimmed",
                size="sm",
            ),
            filters,
            legend,
            dmc.SimpleGrid(
                [
                    dmc.Stack(
                        [
                            dmc.Text("Floor Plan", fw=500),
                            _floor_plan(),
                        ],
                        gap="xs",
                    ),
                    dmc.Stack(
                        [
                            dmc.Text("Campus Map", fw=500),
                            _map_placeholder(),
                        ],
                        gap="xs",
                    ),
                ],
                cols={"base": 1, "md": 2},
                spacing="md",
            ),
        ],
        gap="md",
    )
