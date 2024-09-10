from abc import ABC, abstractmethod

from text_managers.error.error import *
from text_managers.in_game.in_game import *
from text_managers.input.input import *
from text_managers.menu.menu import *


class TextManagerFactory(ABC):
    @abstractmethod
    def create_menu_text_manager(self) -> MenuTextManager:
        pass

    @abstractmethod
    def create_in_game_text_manager(self) -> InGameTextManager:
        pass

    @abstractmethod
    def create_input_text_manager(self) -> InputTextManager:
        pass

    @abstractmethod
    def create_error_text_manager(self) -> ErrorTextManager:
        pass


class RuTextManagerFactory(TextManagerFactory):
    def create_menu_text_manager(self) -> MenuTextManager:
        return RuMenuTextManager()

    def create_in_game_text_manager(self) -> InGameTextManager:
        return RuInGameTextManager()

    def create_input_text_manager(self) -> InputTextManager:
        return RuInputTextManager()

    def create_error_text_manager(self) -> ErrorTextManager:
        return RuErrorTextManager()


class EnTextManagerFactory(TextManagerFactory):
    def create_menu_text_manager(self) -> MenuTextManager:
        return EnMenuTextManager()

    def create_in_game_text_manager(self) -> InGameTextManager:
        return EnInGameTextManager()

    def create_input_text_manager(self) -> InputTextManager:
        return EnInputTextManager()

    def create_error_text_manager(self) -> ErrorTextManager:
        return EnErrorTextManager()


def get_text_manager_factory(lang: str) -> TextManagerFactory:
    match lang:
        case 'en':
            return EnTextManagerFactory()
        case 'ru':
            return RuTextManagerFactory()
        case _:
            return RuTextManagerFactory()
