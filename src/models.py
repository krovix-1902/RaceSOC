from dataclasses import dataclass
from datetime import datetime


@dataclass
class SecurityEvent:
    event_id: str
    timestamp: datetime
    event_type: str
    user: str
    source_ip: str
    source_asset: str
    destination_asset: str
    description: str


@dataclass
class SecurityAlert:
    alert_id: str
    timestamp: datetime
    severity: str
    alert_type: str
    rule_id: str
    source_ip: str
    asset: str
    description: str
    status: str


@dataclass
class SecurityIncident:
    incident_id: str
    title: str
    severity: str
    created_at: datetime
    status: str
    description: str


@dataclass
class Investigation:
    investigation_id: str
    incident_id: str
    timestamp: datetime
    analyst: str
    action: str
    notes: str