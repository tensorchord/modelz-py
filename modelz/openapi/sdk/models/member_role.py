from enum import Enum


class MemberRole(str, Enum):
    MEMBER = "member"
    OWNER = "owner"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
