import json
from datetime import date, datetime

import requests

from ..collection import Collection

TITLE = "City of Calgary"
DESCRIPTION = "Source for Calgary waste Collection"
URL = "https://api.recollect.net"

ICON_MAP = {
    "organics": "mdi:compost",
    "garbage": "mdi:trash-can",
    "recycling": "mdi:recycle",
}

TEST_CASES = {
    "110 9 Ave SE" : {"address": "110 9 Ave SE"},
    "12832 Canso Crescent SW" : {"address": "12832 Canso Crescent SW"},
}

ADDRESS_URL = "https://api.recollect.net/api/areas/Calgary/services/298/address-suggest"

EVENTS_URL = "https://api.recollect.net/api/places/{place_id}/services/298/events"

class Source:
    def __init__(self, address):
        params = {"q": address}
        response = requests.get(ADDRESS_URL, params=params)

        response_ids = response.json()
        if len(response_ids) == 0:
            self.place_id = None
        else:
            self.place_id = response.json()[0]["place_id"]

    def fetch(self):
        if self.place_id is None:
            return []

        current_date = str(date.today())
        params = {
            "after": current_date
        }
        response = requests.get(EVENTS_URL.format(place_id=self.place_id), params=params)

        collections = []
        for event in response.json()["events"]:
            day = event["day"]
            collection_date = datetime.strptime(day, "%Y-%m-%d")
            for flags in event["flags"]:
                collection_type = flags["name"]
                icon = ICON_MAP.get(collection_type)
                collections.append(Collection(collection_date.date(), collection_type, icon=icon))

        return collections

