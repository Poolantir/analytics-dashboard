import dash_mantine_components as dmc
from dash import Dash, html
from firebase_admin import firestore

class MonitoringPage:
    def __init__(self, app: Dash, db: firestore.Client):
        self.app = app
        self.db = db

    def _fetch_collection_docs(self, collection_name: str):
        docs = self.db.collection(collection_name).stream()
        return [{"id": doc.id, **(doc.to_dict() or {})} for doc in docs]

    def layout(self):
        bathrooms = self._fetch_collection_docs("bathrooms")
        sensors = self._fetch_collection_docs("sensors")
        readings = self._fetch_collection_docs("readings")

        def render_docs(title: str, docs: list[dict]):
            if not docs:
                return dmc.Stack(
                    [dmc.Title(title, order=3), dmc.Text("No documents found.")],
                    gap="xs",
                )

            return dmc.Stack(
                [
                    dmc.Title(title, order=3),
                    dmc.Stack(
                        [
                            dmc.Code(
                                str(doc),
                                block=True,
                            )
                            for doc in docs
                        ],
                        gap="xs",
                    ),
                ],
                gap="xs",
            )

        return dmc.Stack(
            [
                dmc.Title("Monitoring", order=2),
                render_docs("Bathrooms", bathrooms),
                render_docs("Sensors", sensors),
                render_docs("Readings", readings),
            ],
            gap="md",
        )