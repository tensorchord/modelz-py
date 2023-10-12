from enum import Enum


class SecretType(str, Enum):
    AWS = "aws"
    DOCKER = "docker"
    GCP = "gcp"

    def __str__(self) -> str:
        return str(self.value)
