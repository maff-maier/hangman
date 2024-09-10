from abc import ABC, abstractmethod

from factory.factory import TextManagerFactory, get_text_manager_factory


class GameTextManager:
    def __init__(self, factory: TextManagerFactory) -> None:
        self.factory = factory
        self._initialize_managers()

    def _initialize_managers(self) -> None:
        self.menu_text_manager = self.factory.create_menu_text_manager()
        self.in_game_text_manager = self.factory.create_in_game_text_manager()
        self.input_text_manager = self.factory.create_input_text_manager()
        self.error_text_manager = self.factory.create_error_text_manager()

    def change_language(self, lang: str) -> None:
        self.factory = get_text_manager_factory(lang=lang)
        self._initialize_managers()

    def print_menu(self) -> None:
        self.menu_text_manager.print_menu()

    def get_menu_option(self) -> str:
        return self.input_text_manager.get_chosen_option()

    def print_language_menu(self) -> None:
        self.menu_text_manager.print_available_languages()

    def get_letter(self) -> str:
        return self.input_text_manager.get_user_letter()

    def print_stage(self, stage: int, limit: int, used: set[str], mask: str) -> None:
        self.in_game_text_manager.print_stage_info(
            stage=stage, limit=limit, used=used, mask=mask)

    def print_invalid_character(self) -> None:
        self.in_game_text_manager.print_invalid_character()

    def print_available_languages(self) -> None:
        self.menu_text_manager.print_available_languages()

    def print_letter_already_used(self) -> None:
        self.in_game_text_manager.print_letter_already_used()

    def print_game_result(self, word: str, is_win: bool) -> None:
        self.in_game_text_manager.print_end_game(word=word, is_win=is_win)

    def print_wrond_command(self) -> None:
        self.menu_text_manager.print_wrong_command()

    def print_file_not_found(self) -> None:
        self.error_text_manager.print_file_not_found()
