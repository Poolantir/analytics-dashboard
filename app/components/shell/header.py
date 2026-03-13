import dash_mantine_components as dmc
from dash import html


PAGE_ORDER = ["Monitoring", "Bathrooms", "Settings"]


def _current_page_from_path(pathname: str) -> str:
    if pathname in ("/", "/monitoring"):
        return "Monitoring"
    if pathname == "/bathrooms":
        return "Bathrooms"
    if pathname == "/settings":
        return "Settings"
    return ""


def _nav_items(pathname: str):
    current_page = _current_page_from_path(pathname or "/")
    items = []
    for page in PAGE_ORDER:
        href = "/monitoring" if page == "Monitoring" else f"/{page.lower()}"
        is_active = page == current_page
        text_color = "#4B382E" if is_active else "#888888"
        font_weight = 700 if is_active else 300

        items.append(
            dmc.Anchor(
                dmc.Text(
                    page,
                    fz={"base": 14, "sm": 12, "md": 14, "lg": 16},
                    c=text_color,
                    fw=font_weight,
                ),
                href=href,
                underline=False,
                style={"textDecoration": "none"},
            )
        )

    return items


def header(pathname: str = "/"):
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

    rhs = dmc.Group(
        _nav_items(pathname),
        h="100%",
        gap="md",
        px="md",
    )

    return dmc.Group(
        [lhs, rhs],
        h="100%",
        align="center",
        justify="space-between",
        px="sm",
    )
