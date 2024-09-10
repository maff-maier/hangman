from abc import ABC, abstractmethod


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
