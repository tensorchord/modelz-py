from enum import Enum


class FrameworkType(str, Enum):
    GRADIO = "gradio"
    MOSEC = "mosec"
    OTHER = "other"
    STREAMLIT = "streamlit"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
