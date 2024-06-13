""" Market Schema """

"""_summary_
This file to abstract any validation logic for the Symbols enums
"""

from enum import Enum


class Symbols(str, Enum):
    AAPL = "AAPL"
    MSFT = "MSFT"
    GOOG = "GOOG"
    AMZN = "AMZN"
    META = "META"

    # Disable validation case insensitive
    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.lower() == value:
                return member
        return None
