import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import html

PAGE_LINKS = {
    "Monitoring": "mdi:monitor-dashboard",
    "Bathrooms": "mdi:toilet",
    "Settings": "tabler:settings",
}

page_items = []
for key, val in PAGE_LINKS.items():
    href = f"/{key.lower()}"
    page_items.append(
        dmc.NavLink(
            label=dmc.Text(key, fz={"base": 18, "sm": 14, "md": 16, "lg": 22}),
            href=href,
            leftSection=DashIconify(icon=val, width=20),
        )
    )


def header():
    lhs = dmc.Group(
        [
            dmc.Image(
                src="/assets/img/poolantir_logo.svg",
                w="120",
                h="45",
                fit="contain",
            ),
        ],
        h="100%",
        px="md",
    )

    menu = dmc.Menu(
        [
            dmc.MenuTarget(
                dmc.ActionIcon(
                    DashIconify(icon="stash:burger-classic-light"),
                    size="lg",
                    variant="subtle",
                ),
            ),
            dmc.MenuDropdown(
                [
                    dmc.MenuLabel("Pages", fz="lg"),
                    *page_items,
                ]
            ),
        ]
    )

    rhs = dmc.Center(
        [menu],
        h="100%",
    )

    return dmc.Group(
        [lhs, rhs],
        h="100%",
        align="center",
        justify="space-between",
        px="sm",
    )
