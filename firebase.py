import firebase_admin
from firebase_admin import credentials, firestore
import uuid
from datetime import datetime

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def create_bathroom(
    bathroom_id: str | None = None,
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
        "name": name,
        "address": address,
        "room_number": room_number,
        "floor": floor,
    }

    db.collection("bathrooms").document(bathroom_id).set(data)
    return bathroom_id


def create_sensor(
    sensor_id: str | None = None,
    name: str | None = None,
    device_type: str | None = None,
    bathroom_id: str | None = None,
    toilet_type: str | None = None,
):
    """
    Create a sensor document in the `sensors` collection.
    """
    if sensor_id is None:
        sensor_id = str(uuid.uuid4())

    data = {
        "id": sensor_id,
        "name": name,
        "device_type": device_type,
        "bathroom_id": bathroom_id,
        "toilet_type": toilet_type,
    }

    db.collection("sensors").document(sensor_id).set(data)
    return sensor_id


def create_reading(
    device_id: str,
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
        "device_id": device_id,
        "start_time": start_time,
        "end_time": end_time,
        "duration": duration,
        "date": date,
    }

    db.collection("readings").document(reading_id).set(data)
    return reading_id


if __name__ == "__main__":

    # Hard-coded example timestamps for a single reading
    start_time = datetime(2025, 1, 1, 12, 0, 0)
    end_time = datetime(2025, 1, 1, 12, 5, 0)
    duration_seconds = (end_time - start_time).total_seconds()
    reading_date = start_time.date().isoformat()

    b_id = create_bathroom(
        name="Test Bathroom",
        address="123 Main St",
        room_number="101",
        floor="1",
    )

    s_id = create_sensor(
        name="Door Sensor 1",
        device_type="door",
        bathroom_id=b_id,
        toilet_type="unisex",
    )

    r_id = create_reading(
        device_id=s_id,
        start_time=start_time,
        end_time=end_time,
        duration=duration_seconds,
        date=reading_date,
    )

    print("Created bathroom:", b_id)
    print("Created sensor:", s_id)
    print("Created reading:", r_id)