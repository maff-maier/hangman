from typing import Iterable

from validators.alphabet import EnAlphabetValidator, RuAlphabetValidator
from validators.length import LengthValidator
from validators.validator import Validator


def get_validators(lang: str) -> Iterable[Validator]:
    validators = list()
    match lang:
        case 'ru':
            validators.append(RuAlphabetValidator())
        case 'en':
            validators.append(EnAlphabetValidator())
        case _:
            validators.append(RuAlphabetValidator())

    validators.append(LengthValidator())
    return validators


class ValidatorManager(Validator):
    def __init__(self) -> None:
        self._validators = get_validators(lang='ru')

    def change_language(self, lang: str) -> None:
        self._validators = get_validators(lang=lang)

    def validate(self, letter: str) -> bool:
        return all([validator.validate(letter=letter) for validator in self._validators])
