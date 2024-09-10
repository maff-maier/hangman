from abc import ABC, abstractmethod

from validators.validator import Validator


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
