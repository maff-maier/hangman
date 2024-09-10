from typing import Protocol


class Validator(Protocol):
    def validate(self, letter: str) -> bool:
        pass
