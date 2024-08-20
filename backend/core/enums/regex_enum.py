from enum import Enum


class RegexEnum(Enum):
    NAME = (
        r'^[A-Z][a-zA-Z]{1,19}$',
        'First letter uppercase, min 2, max 20'
    )
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])(\S){8,18}$',
        [
            'Password must contain at least 1 number (1-9)',
            'Password must contain at least 1 uppercase letter',
            'Password must contain at least 1 lowercase letter',
            'Password must contain at least 1 special character',
            'Password must contain min 8 max 16 characters without spaces'
        ]
    )
    BRAND = (
        r'^[A-Z](?=.*[A-Z])?(?=.*[a-z])?(\S){3,20}$',
        [
            'Brand name must start with capital letter',
            'Brand name must contain min 3 max 20 characters without spaces'
        ],
    )

    def __init__(self, pattern: str, msg: str|list[str]):
        self.pattern = pattern
        self.msg = msg
