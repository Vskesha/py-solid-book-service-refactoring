from .book import Book
from .display_types import DISPLAY_MAP
from .print_types import PRINT_MAP
from .serialize_types import SERIALIZE_MAP


class BookService:
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self, method_type: str) -> None:
        if method_type not in DISPLAY_MAP:
            raise ValueError(f"Unknown display type: {method_type}")
        display_type = DISPLAY_MAP[method_type]()
        display_type.display(self.book)

    def print(self, method_type: str) -> None:
        if method_type not in PRINT_MAP:
            raise ValueError(f"Unknown print type: {method_type}")
        print_type = PRINT_MAP[method_type]()
        print_type.print(self.book)

    def serialize(self, method_type: str) -> str:
        if method_type not in SERIALIZE_MAP:
            raise ValueError(f"Unknown serialize type: {method_type}")
        serialize_type = SERIALIZE_MAP[method_type]()
        return serialize_type.serialize(self.book)
