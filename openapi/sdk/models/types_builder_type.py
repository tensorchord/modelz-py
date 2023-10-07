from enum import Enum


class TypesBuilderType(str, Enum):
    DOCKERFILE = "Dockerfile"
    ENVD = "envd"
    IMAGE = "image"

    def __str__(self) -> str:
        return str(self.value)
