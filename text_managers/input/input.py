from abc import ABC, abstractmethod


class InputTextManager(ABC):
    @abstractmethod
    def get_chosen_option(self) -> str:
        pass

    @abstractmethod
    def get_user_letter(self) -> str:
        pass


class RuInputTextManager(InputTextManager):
    def get_chosen_option(self) -> str:
        return input('Ваш выбор: ').lower()

    def get_user_letter(self) -> str:
        return input('Введите букву: ').lower()


class EnInputTextManager(InputTextManager):
    def get_chosen_option(self) -> str:
        return input('Your choice: ').lower()

    def get_user_letter(self) -> str:
        return input('Your letter: ').lower()
