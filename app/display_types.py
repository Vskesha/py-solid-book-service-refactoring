from abc import abstractmethod, ABC

from .book import Book


class IDisplayType(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayType(IDisplayType):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayType(IDisplayType):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


DISPLAY_MAP = {
    "console": ConsoleDisplayType,
    "reverse": ReverseDisplayType,
}
