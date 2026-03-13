from dash import Dash, html, dcc, Input, Output
import dash_mantine_components as dmc
import os
from pathlib import Path

from pages.monitoring import monitoring_layout
from pages.bathrooms import bathrooms_layout
from pages.settings import settings_layout

from components.shell.header import header
from components.shell.footer import footer

HOST = os.getenv("HOST", "0.0.0.0")
DASH_PORT = os.getenv("DASH_PORT", "8000")

app = Dash(
    name="Poolantir",
    assets_folder=str(Path(__file__).parent / "assets"),
    suppress_callback_exceptions=True,
)

app.title = "Poolantir"

app.layout = dmc.MantineProvider(
    theme={
        "defaultRadius": "sm",
        "components": {
            "Card": {
                "defaultProps": {
                    "shadow": "xs",
                    "radius": "sm",
                }
            },
        },
    },
    children=[
        dcc.Location(id="url"),
        dmc.AppShell(
            [
                dmc.AppShellHeader(
                    dmc.Box(
                        id="app-header",
                        h="100%",
                    )
                ),
                dmc.AppShellMain(
                    dmc.Box(
                        id="page-content",
                        py="sm",
                        px="sm",
                    ),
                ),
                footer(),
            ],
            header={"height": 60},
        ),
    ],
)


@app.callback(
    Output("app-header", "children"),
    Input("url", "pathname"),
)
def update_header(pathname):
    return header(pathname or "/")


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname in ("/", "/monitoring"):
        return monitoring_layout()
    elif pathname == "/bathrooms":
        return bathrooms_layout()
    elif pathname == "/settings":
        return settings_layout()
    return html.Div(
        dmc.Stack(
            [
                dmc.Title("404", order=1),
                dmc.Text("Page not found"),
            ],
            align="center",
            justify="center",
            h="60vh",
        )
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        port=DASH_PORT,
        host=HOST,
    )