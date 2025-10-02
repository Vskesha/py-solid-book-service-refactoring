from abc import ABC, abstractmethod

from .book import Book


class IPrintType(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrintType(IPrintType):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrintType(IPrintType):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


PRINT_MAP = {
    "console": ConsolePrintType,
    "reverse": ReversePrintType,
}
