import random
from enum import Enum

from text_manager import GameTextManager, get_text_manager_factory
from validators import ValidatorManager


class WordManager:
    def __init__(self, word: str, mask_symbol: str = '_') -> None:
        self.__word = word
        self.mask_symbol = mask_symbol
        self.mask = [mask_symbol] * len(word)

    def get_mask(self) -> str:
        return ' '.join(self.mask)

    @property
    def mask_symbol(self) -> str:
        return self._mask_symbol

    @mask_symbol.setter
    def mask_symbol(self, symbol: str) -> None:
        self._mask_symbol = symbol

    def is_reveal_word(self) -> bool:
        return self.mask_symbol not in self.mask

    def is_letter_in_word(self, letter: str) -> bool:
        return letter in self.__word

    def reveal_letter(self, letter: str) -> str:
        for idx, char in enumerate(self.__word):
            if char == letter:
                self.mask[idx] = letter

    def get_hidden_word(self) -> str:
        return self.__word


class MainCommands(Enum):
    START = '1'
    CHANGE_LANGUAGE = '2'
    END = '3'


class LangCommands(Enum):
    RU = '1'
    EN = '2'


class GameManager:
    def __init__(self, file: str = 'glossary\\ru.txt') -> None:
        self.file = file

    @property
    def filename(self) -> str:
        return self.file

    @filename.setter
    def filename(self, lang: str) -> None:
        self.file = f'glossary\\{lang}.txt'

    def _load_words(self, text_manager: GameTextManager) -> list[str]:
        try:
            with open(file=self.file, mode='r', encoding='utf-8') as file:
                return file.readlines()
        except FileNotFoundError:
            text_manager.print_file_not_found()
            exit(1)
        except Exception as ex:
            print(ex)
            exit(-1)

    def _pick_word(self, text_manager: GameTextManager) -> str:
        return random.choice(seq=self._load_words(text_manager=text_manager)).replace('\n', '')

    def change_language(self, text_manager: GameTextManager, validator: ValidatorManager) -> None:
        text_manager.print_available_languages()

        selected = ''
        while True:
            match text_manager.input_text_manager.get_chosen_option():
                case LangCommands.EN.value:
                    selected = LangCommands.EN.name.lower()
                    break
                case LangCommands.RU.value:
                    selected = LangCommands.RU.name.lower()
                    break
                case _:
                    text_manager.print_wrong_command()

        text_manager.change_language(lang=selected)
        validator.change_language(lang=selected)
        self.filename = selected

    def start_game(self, text_manager: GameTextManager, word_manager: WordManager, validator: ValidatorManager) -> None:
        mistakes = 0
        mistakes_limit = 6
        used = set()

        while mistakes < mistakes_limit and not word_manager.is_reveal_word():
            text_manager.print_stage(
                stage=mistakes, limit=mistakes_limit, used=used, mask=word_manager.get_mask())

            letter = ''
            while True:
                letter = text_manager.get_letter()

                if not validator.validate(letter=letter):
                    text_manager.print_invalid_character()
                    continue

                if letter in used:
                    text_manager.print_letter_already_used()
                else:
                    break

            if word_manager.is_letter_in_word(letter=letter):
                word_manager.reveal_letter(letter=letter)
            else:
                mistakes += 1

            used.add(letter)

        is_win = mistakes != mistakes_limit

        text_manager.print_game_result(
            word=word_manager.get_hidden_word(), is_win=is_win)


class GameConfig:
    def __init__(self, mistakes_limit: int = 6, mask_symbol: str = '_') -> None:
        self.limit = mistakes_limit
        self._mask_symbol = mask_symbol

    @property
    def mistakes_limit(self) -> int:
        return self.limit

    @mistakes_limit.setter
    def mistakes_limit(self, limit: int) -> None:
        self.limit = limit

    @property
    def mask_symbol(self) -> str:
        return self._mask_symbol

    @mask_symbol.setter
    def mask_symbol(self, symbol: str) -> None:
        self._mask_symbol = symbol


class Game:
    def play(self) -> None:
        text_manager = GameTextManager(
            factory=get_text_manager_factory(lang='ru'))
        game_manager = GameManager()
        validator = ValidatorManager()

        while True:
            text_manager.print_menu()
            inp = text_manager.get_menu_option()

            match inp:
                case MainCommands.START.value:
                    game_manager.start_game(text_manager=text_manager, word_manager=WordManager(
                        word=game_manager._pick_word(text_manager=text_manager)), validator=validator)
                case MainCommands.CHANGE_LANGUAGE.value:
                    game_manager.change_language(
                        text_manager=text_manager, validator=validator)
                case MainCommands.END.value:
                    break
                case _:
                    text_manager.print_wrond_command()


if __name__ == '__main__':
    game = Game()
    game.play()
