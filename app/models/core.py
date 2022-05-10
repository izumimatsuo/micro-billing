import enum


# ISO 4217
class CurrencyType(str, enum.Enum):
    jpy = "jpy"
    usd = "usd"
