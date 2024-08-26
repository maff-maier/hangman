import random
from typing import Set
from enum import Enum


class TextManager:
    gallows_stages = [
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
           /|\\ |
                |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
           /|\\ |
           /    |
                |
            --------\n
        """,
        """
            -----
            |   |
            O   |
           /|\\ |
           / \\ |
                |
            --------\n
        """,
    ]

    @staticmethod
    def print_options() -> None:
        print('Выберите действие:\n\n(н) Новая игра\n(в) Выйти')

    @staticmethod
    def get_choice_letter() -> str:
        return 'Введите букву: '

    @staticmethod
    def get_menu_choice() -> str:
        return 'Ваш выбор: '

    @classmethod
    def print_gallows(cls, stage: int) -> None:
        print(cls.gallows_stages[stage])

    @staticmethod
    def print_letter_already_used() -> None:
        print('Вы уже вводили эту букву, введите другую')

    @classmethod
    def print_used_letter(cls, used: Set[str]) -> None:
        used_letters = ' '.join(used)
        print(f'Использованные буквы: {used_letters}')

    @classmethod
    def print_stage(cls, mask: str, stage: int, limit: int,  used: Set[str]) -> None:
        print(mask)
        cls.print_gallows(stage=stage)
        print(
            f'Количество ошибок: {stage}, количество допустимых ошибок - {limit-1}')
        cls.print_used_letter(used=used)

    @staticmethod
    def print_hidden_word(word: str) -> None:
        print(f'Загаданное слово: {word}\n')

    @staticmethod
    def print_lose() -> None:
        print('\nСожалеем, Вы проиграли!')

    @staticmethod
    def print_win() -> None:
        print('\nПоздравляем! Вы выиграли!')

    @staticmethod
    def print_file_not_found() -> None:
        print('Файл с указанным именем не найден. Проверьте правильность названия или целостность файлов.')


class Validator:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    @staticmethod
    def is_single_char(char: str) -> bool:
        return len(char) == 1

    @classmethod
    def is_valid_char(cls, char: str) -> bool:
        return cls.is_single_char(char=char) and char in cls.alphabet


class WordManager:
    def __init__(self, word: str) -> None:
        self.__word = word
        self.mask = ['_'] * len(word)

    def get_mask(self) -> str:
        return ' '.join(self.mask)

    def is_letter_in_word(self, letter: str) -> bool:
        return letter in self.__word

    def reveal_letter(self, letter: str) -> str:
        for idx, char in enumerate(self.__word):
            if char == letter:
                self.mask[idx] = letter

    def get_hidden_word(self) -> str:
        return self.__word


class Commands(Enum):
    START = 'н'
    END = 'в'


class Game:
    def __init__(self, file: str = 'glossary.txt') -> None:
        self.__file = file
        self.__words = self.__load_words(file=file)

    def get_words(self) -> list[str]:
        return self.__words

    def play(self) -> None:
        while True:
            TextManager.print_options()

            match (inp := input(TextManager.get_menu_choice()).lower()):
                case Commands.START.value:
                    pass
                case Commands.END.value:
                    break
                case _:
                    continue

            mistakes = 0
            mistakes_limit = 6
            used = set()

            word_manager = WordManager(word=self.__pick_word())

            while mistakes < mistakes_limit and '_' in word_manager.get_mask():
                TextManager.print_stage(mask=word_manager.get_mask(
                ), stage=mistakes, limit=mistakes_limit, used=used)

                letter = ''
                while True:
                    letter = input(TextManager.get_choice_letter()).lower()

                    if letter in used:
                        TextManager.print_letter_already_used()
                        continue

                    if Validator.is_valid_char(letter):
                        break

                if word_manager.is_letter_in_word(letter=letter):
                    word_manager.reveal_letter(letter=letter)
                else:
                    mistakes += 1

                used.add(letter)

            if mistakes == mistakes_limit:
                TextManager.print_lose()
            else:
                TextManager.print_win()

            TextManager.print_hidden_word(word=word_manager.get_hidden_word())

    def __load_words(self, file: str) -> list[str]:
        try:
            with open(file=file, mode='r', encoding='utf-8') as file:
                return file.readlines()
        except FileNotFoundError:
            TextManager.print_file_not_found()
            exit(1)

    def __pick_word(self) -> str:
        return random.choice(seq=self.get_words()).replace('\n', '')


if __name__ == '__main__':
    game = Game()
    game.play()
