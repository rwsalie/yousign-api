from enum import StrEnum
from dataclasses import dataclass


@dataclass
class Info:
    first_name: str
    last_name: str
    email: str
    locale: str


class DeliveryMode(StrEnum):
    NONE = 'none',
    EMAIL = 'email'
