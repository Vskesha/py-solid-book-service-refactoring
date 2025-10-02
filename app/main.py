from .book import Book
from .book_service import BookService


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    book_service = BookService(book)

    for cmd, method_type in commands:
        command_method = getattr(book_service, cmd)
        result = command_method(method_type)
        if cmd == "serialize":
            return result
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
