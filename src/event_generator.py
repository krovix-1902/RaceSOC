import random
from datetime import datetime

from models import SecurityEvent


USERS = [
    "engineer01",
    "engineer02",
    "strategist01",
    "analyst01",
]

ASSETS = [
    "ENGINEER-LAPTOP-01",
    "ENGINEER-LAPTOP-02",
    "TELEMETRY-SERVER-01",
    "GIT-SERVER-01",
    "RACE-STRATEGY-01",
    "CLOUD-STORAGE-01",
]

EVENT_TYPES = [
    "LOGIN_SUCCESS",
    "VPN_CONNECTION",
    "FILE_ACCESS",
    "GIT_ACCESS",
    "TELEMETRY_ACCESS",
    "NETWORK_CONNECTION",
]


def generate_event(event_id: str) -> SecurityEvent:
    """Generate one normal security event."""

    user = random.choice(USERS)
    asset = random.choice(ASSETS)
    event_type = random.choice(EVENT_TYPES)

    return SecurityEvent(
        event_id=event_id,
        timestamp=datetime.now(),
        event_type=event_type,
        user=user,
        source_ip=f"192.168.10.{random.randint(10, 250)}",
        source_asset=asset,
        destination_asset=asset,
        description=f"{user} performed {event_type} on {asset}",
    )

if __name__ == "__main__":
    for number in range(1, 11):
        event = generate_event(f"EVT-{number:06d}")
        print(event)