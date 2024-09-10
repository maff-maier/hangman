from validators.validator import Validator


class LengthValidator(Validator):
    def validate(self, letter: str) -> bool:
        return len(letter) == 1
