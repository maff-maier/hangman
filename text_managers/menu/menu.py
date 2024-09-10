from abc import ABC, abstractmethod


class MenuTextManager(ABC):
    @abstractmethod
    def print_menu(self) -> None:
        pass

    @abstractmethod
    def print_wrong_command(self) -> None:
        pass

    @abstractmethod
    def print_available_languages(self) -> None:
        pass


class RuMenuTextManager(MenuTextManager):
    def print_menu(self) -> None:
        print('\nВыберите действие:\n1.Новая игра\n2.Сменить язык\n3.Выйти')

    def print_wrong_command(self) -> None:
        print('Неверная команда. Выберите один из предложенных вариантов!')

    def print_available_languages(self) -> None:
        print('\nВыберите один из предложенных языков:\n1. ru\n2. en\nПо умолчанию выбран русский.')


class EnMenuTextManager(MenuTextManager):
    def print_menu(self) -> None:
        print('\nChoice option:\n1.New game\n2.Change language\n3.Exit')

    def print_wrong_command(self) -> None:
        print('Invalid command! Select one of the suggested ones!')

    def print_available_languages(self) -> None:
        print('\nChoose one of languages above:\n1. ru\n2. en\nRussian is the default language.')
