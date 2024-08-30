from typing import Iterable, Protocol
from abc import abstractmethod, ABC


class Validator(Protocol):
    def validate(self, letter: str) -> bool:
        pass


class LengthValidator(Validator):
    def validate(self, letter: str) -> bool:
        return len(letter) == 1


class AlphabetValidator(Validator, ABC):
    @abstractmethod
    def validate(self, letter: str) -> bool:
        pass


class RuAlphabetValidator(AlphabetValidator):
    def validate(self, letter: str) -> bool:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        return letter in alphabet


class EnAlphabetValidator(AlphabetValidator):
    def validate(self, letter: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        return letter in alphabet



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
