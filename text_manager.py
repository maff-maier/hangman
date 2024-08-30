from abc import ABC, abstractmethod


class GallowsManager:
    stages = [
        """
            -----
            |   |
                |
                |
                |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
                |
                |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
            |   |
                |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
           /|   |
                |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
                |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
           /    |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
           /|\\  |
           / \\ |
                |
            --------\n
        """,
    ]

    @classmethod
    def print_gallows_stage(cls, stage: int):
        print(cls.stages[stage])


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


class ErrorTextManager(ABC):
    @abstractmethod
    def print_file_not_found(self) -> None:
        pass


class RuErrorTextManager(ErrorTextManager):
    def print_file_not_found(self) -> None:
        print('Файл с таким именем не найдет. Проверьте правильность названия файла.')


class EnErrorTextManager(ErrorTextManager):
    def print_file_not_found(self) -> None:
        print('File not found. Make sure that filename is correct.')


class InGameTextManager(ABC):
    def print_stage_info(self, stage: int, limit: int, used: set[str], mask: str) -> None:
        GallowsManager.print_gallows_stage(stage=stage)
        self._print_hidden_word_mask(mask=mask)
        self._print_mistakes_info(mistakes=stage, limit=limit)
        self._print_used_letters(used=used)

    def print_end_game(self, word: str, is_win: bool) -> None:
        if is_win:
            self._print_win()
        else:
            self._print_lose()
        self._print_hidden_word(word=word)

    @abstractmethod
    def _print_mistakes_info(self, mistakes: int, limit: int) -> None:
        pass

    @abstractmethod
    def _print_used_letters(self, used: set[str]) -> None:
        pass

    @abstractmethod
    def _print_win(self) -> None:
        pass

    @abstractmethod
    def _print_lose(self) -> None:
        pass

    @abstractmethod
    def _print_hidden_word(self, word: str) -> None:
        pass

    @abstractmethod
    def print_letter_already_used(self) -> None:
        pass

    @abstractmethod
    def _print_hidden_word_mask(self, word: str) -> None:
        pass

    @abstractmethod
    def print_invalid_character(self) -> None:
        pass


class RuInGameTextManager(InGameTextManager):
    def _print_mistakes_info(self, mistakes: int, limit: int) -> None:
        print(
            f'Количество ошибок - {mistakes}, количество допустимых ошибок - {limit-1}')

    def _print_used_letters(self, used: set[str]) -> None:
        used = ' '.join(used)
        print(f'Использованные буквы: {used}')

    def _print_win(self) -> None:
        print('\nПоздравляем! Вы победили!')

    def _print_lose(self) -> None:
        print('\nВы проиграли!')

    def _print_hidden_word(self, word: str) -> None:
        print(f'Загаданное слово: {word}')

    def print_letter_already_used(self) -> None:
        print('Вы уже вводили эту букву, введите другую')

    def _print_hidden_word_mask(self, mask: str) -> None:
        print(f'{mask}')

    def print_invalid_character(self) -> None:
        print('Некорретный ввод! Повторите попытку!')


class EnInGameTextManager(InGameTextManager):
    def _print_mistakes_info(self, mistakes: int, limit: int) -> None:
        print(f'Mistakes - {mistakes}, mistakes limit - {limit-1}')

    def _print_used_letters(self, used: set[str]) -> None:
        used = ' '.join(used)
        print(f'Used letters: {used}')

    def _print_win(self) -> None:
        print('\nCongratulations! You WON!')

    def _print_lose(self) -> None:
        print('\nYou LOST!')

    def _print_hidden_word(self, word: str) -> None:
        print(f'Hidden word: {word}')

    def print_letter_already_used(self) -> None:
        print('Letter already used! Please input other letter')

    def _print_hidden_word_mask(self, mask: str) -> None:
        print(f'{mask}')

    def print_invalid_character(self) -> None:
        print('Invalid character! Please try again!')


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
