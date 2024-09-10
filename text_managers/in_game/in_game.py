from abc import ABC, abstractmethod

from text_managers.gallows.gallows import GallowsManager


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
