import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

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


def generate_event(event_id: str, timestamp: datetime) -> SecurityEvent:
    """Generate one normal security event."""

    user = random.choice(USERS)
    asset = random.choice(ASSETS)
    event_type = random.choice(EVENT_TYPES)

    return SecurityEvent(
        event_id=event_id,
        timestamp=timestamp,
        event_type=event_type,
        user=user,
        source_ip=f"192.168.10.{random.randint(10, 250)}",
        source_asset=asset,
        destination_asset=asset,
        description=f"{user} performed {event_type} on {asset}",
    )


def save_events(events: list[SecurityEvent], output_file: Path) -> None:
    """Save security events to a CSV file."""

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "event_id",
            "timestamp",
            "event_type",
            "user",
            "source_ip",
            "source_asset",
            "destination_asset",
            "description",
        ])

        for event in events:
            writer.writerow([
                event.event_id,
                event.timestamp.isoformat(),
                event.event_type,
                event.user,
                event.source_ip,
                event.source_asset,
                event.destination_asset,
                event.description,
            ])


if __name__ == "__main__":
    events = []

    start_time = datetime.now() - timedelta(hours=2)

    for number in range(1, 101):
        timestamp = start_time + timedelta(minutes=number)

        event = generate_event(
            f"EVT-{number:06d}",
            timestamp,
        )

        events.append(event)

    output_path = Path("data/events.csv")

    save_events(events, output_path)

    print(f"Generated {len(events)} security events.")
    print(f"Saved to: {output_path}")