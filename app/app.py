from dash import Dash, html, dcc, Input, Output
import dash_mantine_components as dmc
import os
from pathlib import Path

import firebase_admin
from firebase_admin import credentials, firestore

from pages.monitoring import MonitoringPage
# from pages.bathrooms import bathrooms_layout
# from pages.settings import settings_layout

from components.shell.header import header
from components.shell.footer import footer

# ============================
#         ENVIRONMENT
# ============================
HOST = os.getenv("HOST", "0.0.0.0")
DASH_PORT = os.getenv("DASH_PORT", "8000")

# ============================
#    FIREBASE CONNECTION
# ============================
cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# ============================
#    INITIALIZE DASH APP
# ============================
app = Dash(
    name="Poolantir",
    assets_folder=str(Path(__file__).parent / "assets"),
    suppress_callback_exceptions=True,
)

app.title = "Poolantir"

# ============================
#        PAGE OBJECTS
# ============================
monitoring_page_obj = MonitoringPage(app=app, db=db)
# bathrooms_page_obj = BathroomsPage(app=app, db=db)
# settings_page_obj = SettingsPage(app=app, db=db)

# ============================
#           LAYOUT
# ============================
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
                    header()
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

# ============================
#           ROUTING
# ============================
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname in ("/", "/monitoring"):
        return monitoring_page_obj.layout()
    # elif pathname == "/bathrooms":
    #     return bathrooms_page_obj.layout()
    # elif pathname == "/settings":
    #     return settings_page_obj.layout()
    else:
        return html.Div("404")


if __name__ == "__main__":
    app.run(
        debug=True,
        port=DASH_PORT,
        host=HOST,
    )