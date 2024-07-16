import random
from typing import Set


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

    @classmethod
    def print_control_menu(cls) -> str:
        cls.print_options()
        return input('Ваш выбор: ').lower()
    
    @classmethod
    def print_options(cls) -> None:
        print('Выберите действие:\n\n(н) Новая игра\n(в) Выйти')

    @classmethod
    def get_choice_letter(cls) -> str:
        return 'Введите букву: '

    @classmethod
    def print_gallows(cls, stage: int) -> None:
        print(cls.gallows_stages[stage])

    @classmethod
    def letter_already_used(cls) -> None:
        print('Вы уже вводили эту букву, введите другую')

    @classmethod
    def print_used_letter(cls, used: Set[str]) -> None:
        used_letters = ' '.join(used)
        print(f'Использованные буквы: {used_letters}')
        
    @classmethod
    def print_stage(cls, mask: str, stage: int, limit: int,  used: Set[str]) -> None:
        print(mask)
        cls.print_gallows(stage=stage)
        print(f'Количество ошибок: {stage}, количество допустимых ошибок - {limit-1}')
        cls.print_used_letter(used=used)
    
    @classmethod
    def print_hidden_word(cls, word: str) -> None:
        print(f'Загаданное слово: {word}\n')
    
    @classmethod
    def lose_message(cls) -> None:
        print('Сожалеем, Вы проиграли!')
        
    @classmethod
    def win_message(cls) -> None:
        print('Поздравляем! Вы выиграли!')
    

class Validator:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    @classmethod
    def is_single_char(cls, char: str) -> bool:
        return len(char) == 1

    @classmethod
    def is_valid_char(cls, char: str) -> bool:
        return cls.is_single_char(char=char) and char in cls.alphabet


class WordMask:
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


class Game:
    def __pick_word(self) -> str:
        words = []

        with open(file='glossary.txt', mode='r', encoding='utf-8') as file:
            words = file.readlines()
            
        return random.choice(seq=words).replace('\n', '')

    def play(self):
        while True:
            if (inp := TextManager.print_control_menu()) != 'н' and inp != 'в':
                continue
            elif inp == 'в':
                break
            
            mistakes = 0
            mistakes_limit = 6
            used = set()

            word_mask = WordMask(word=self.__pick_word())

            while mistakes < mistakes_limit and '_' in word_mask.get_mask():
                TextManager.print_stage(mask=word_mask.get_mask(), stage=mistakes, limit=mistakes_limit, used=used)

                letter = ''
                while True:
                    letter = input(TextManager.get_choice_letter()).lower()

                    if letter in used:
                        TextManager.letter_already_used()
                        continue
                    
                    if Validator.is_valid_char(letter):
                        break


                if word_mask.is_letter_in_word(letter=letter):
                    word_mask.reveal_letter(letter=letter)
                else:
                    mistakes += 1

                used.add(letter)
            else:
                if mistakes == mistakes_limit:
                    TextManager.lose_message()
                else:
                    TextManager.win_message()
                    
                TextManager.print_hidden_word(word=word_mask.get_hidden_word())
                    


if __name__ == '__main__':
    game = Game()
    game.play()
