import dash_mantine_components as dmc
from dash import Dash
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
        toilets = self._fetch_collection_docs("toilets")
        sensors = self._fetch_collection_docs("sensors")
        readings = self._fetch_collection_docs("readings")

        def render_table(title: str, docs: list[dict]):
            if not docs:
                return dmc.Stack(
                    [dmc.Title(title, order=3), dmc.Text("No documents found.")],
                    gap="xs",
                )

            # Collect all keys across documents to form table headers
            all_keys: set[str] = set()
            for doc in docs:
                all_keys.update(doc.keys())

            # Ensure "id" appears first if present
            headers = sorted(all_keys - {"id"})
            if "id" in all_keys:
                headers = ["id"] + headers

            table_body = [
                [str(doc.get(key, "")) for key in headers]
                for doc in docs
            ]

            return dmc.Stack(
                [
                    dmc.Title(title, order=3),
                    dmc.TableScrollContainer(
                        dmc.Table(
                            data={
                                "head": headers,
                                "body": table_body,
                            },
                            striped=True,
                            highlightOnHover=True,
                            withTableBorder=True,
                            withColumnBorders=True,
                        ),
                        minWidth="100%",
                        type="scrollarea",
                    )
                ],
                gap="xs",
            )

        return dmc.Stack(
            [
                dmc.Title("Monitoring", order=2),
                render_table("Bathrooms", bathrooms),
                render_table("Toilets", toilets),
                render_table("Sensors", sensors),
                render_table("Readings", readings),
            ],
            gap="md",
        )