from enum import Enum


class ReadinessStatus(str, Enum):
    ok = "ok"
    no = "no"
