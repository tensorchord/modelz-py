from enum import Enum


class ServerResource(str, Enum):
    CPU_4C_16G = "cpu-4c-16g"
    NVIDIA_ADA_L4_2_24C_96G = "nvidia-ada-l4-2-24c-96g"
    NVIDIA_ADA_L4_4_48C_192G = "nvidia-ada-l4-4-48c-192g"
    NVIDIA_ADA_L4_8C_32G = "nvidia-ada-l4-8c-32g"
    NVIDIA_AMPERE_A100_40G_12C_85G = "nvidia-ampere-a100-40g-12c-85g"
    NVIDIA_TESLA_T4_4C_16G = "nvidia-tesla-t4-4c-16g"

    def __str__(self) -> str:
        return str(self.value)
