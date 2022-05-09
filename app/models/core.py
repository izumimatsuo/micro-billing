import enum


# ISO 4217
class Currency(str, enum.Enum):
    jpy = "jpy"
    usd = "usd"
