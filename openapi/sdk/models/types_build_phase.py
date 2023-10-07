from enum import Enum


class TypesBuildPhase(str, Enum):
    FAILED = "Failed"
    PENDING = "Pending"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"

    def __str__(self) -> str:
        return str(self.value)
