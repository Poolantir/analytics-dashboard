import firebase_admin
from firebase_admin import credentials, firestore
import uuid
from datetime import datetime
import argparse

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def clear_database():
    """
    Remove all documents from all top-level collections in the Firestore database.
    This is intended for development/testing use only.
    """
    for collection_ref in db.collections():
        docs = list(collection_ref.stream())
        for doc in docs:
            doc.reference.delete()


def create_bathroom(
    bathroom_id: str | None = None,
    gender: str | None = None,
    name: str | None = None,
    address: str | None = None,
    room_number: str | None = None,
    floor: str | None = None,
):
    """
    Create a bathroom document in the `bathrooms` collection.
    """
    if bathroom_id is None:
        bathroom_id = str(uuid.uuid4())

    data = {
        "id": bathroom_id,
        "gender": gender,
        "address": address,
        "room_number": room_number,
        "floor": floor,
    }

    db.collection("bathrooms").document(bathroom_id).set(data)
    return bathroom_id

def create_toilet(
    toilet_id: str | None = None,
    toilet_type: str | None = None,
    model: str | None = None,
    bathroom_id: str | None = None,
):
    """
    Create a toilet document in the `toilets` collection.
    """
    if toilet_id is None:
        toilet_id = str(uuid.uuid4())

    data = {
        "id": toilet_id,
        "toilet_type": toilet_type,
        "model": model,
        "bathroom_id": bathroom_id,
    }

    db.collection("toilets").document(toilet_id).set(data)
    return toilet_id


def create_sensor(
    sensor_id: str | None = None,
    name: str | None = None,
    toilet_id: str | None = None,
):
    """
    Create a sensor document in the `sensors` collection.
    """
    if sensor_id is None:
        sensor_id = str(uuid.uuid4())

    data = {
        "id": sensor_id,
        "name": name,
        "toilet_id": toilet_id,
    }

    db.collection("sensors").document(sensor_id).set(data)
    return sensor_id


def create_reading(
    sensor_id: str,
    start_time,
    end_time,
    duration: float,
    date,
):
    """
    Create a reading document in the `readings` collection.

    `start_time`, `end_time`, and `date` can be Python `datetime` objects
    or ISO8601 strings; Firestore will store them as provided.
    """
    reading_id = str(uuid.uuid4())

    data = {
        "id": reading_id,
        "sensor_id": sensor_id,
        "start_time": start_time,
        "end_time": end_time,
        "duration": duration,
        "date": date,
    }

    db.collection("readings").document(reading_id).set(data)
    return reading_id


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Firestore bathroom/toilet/sensor utilities."
    )
    parser.add_argument(
        "-c",
        "--clear",
        action="store_true",
        help="Clear all Firestore data and exit.",
    )
    args = parser.parse_args()

    if args.clear:
        clear_database()
        print("All Firestore data cleared.")
    else:
        # Create one bathroom record.
        bathroom_id = create_bathroom(
            gender="unisex",
            name="Main Hall Bathroom",
            address="123 Main St",
            room_number="101",
            floor="1",
        )

        # Create six toilets (3 urinals and 3 toilets), each with an attached sensor.
        toilet_specs = (
            [("urinal", f"Urinal {i + 1}") for i in range(3)]
            + [("toilet", f"Toilet {i + 1}") for i in range(3)]
        )

        for toilet_type, model in toilet_specs:
            t_id = create_toilet(
                toilet_type=toilet_type,
                model=model,
                bathroom_id=bathroom_id,
            )
            create_sensor(
                name=f"{model} Sensor",
                toilet_id=t_id,
            )