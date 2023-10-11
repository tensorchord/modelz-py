from enum import Enum


class UserState(str, Enum):
    IN_WHITE_LIST = "in-white-list"
    NORMAL = "normal"
    NO_PAYMENT_METHOD = "no-payment-method"
    PAST_DUE = "past-due"
    SPEND_LIMIT_EXCEEDED = "spend-limit-exceeded"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
