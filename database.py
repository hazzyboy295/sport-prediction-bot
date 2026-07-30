import json
import os

DATABASE_FILE = "database.json"

DEFAULT_DATA = {
    "users": [],
    "vip_users": [],
    "free_prediction": "No free prediction available.",
    "vip_prediction": "No VIP prediction available.",
    "results": "No results available."
}


def load_data():
    if not os.path.exists(DATABASE_FILE):
        save_data(DEFAULT_DATA)

    with open(DATABASE_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)
