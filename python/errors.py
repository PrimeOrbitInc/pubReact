import enum


class Err(enum.Enum):

    OE0004 = [
        "Type error: %s",
        ["Traceback when try to set wrong value for enum type"],
        ["'unexpected' is not a valid ConditionTypes"]
    ]
