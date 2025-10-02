import json
from abc import ABC, abstractmethod
from xml.etree import ElementTree

from .book import Book


class ISerializeType(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JSONSerializeType(ISerializeType):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializeType(ISerializeType):
    def serialize(self, book: Book) -> str:
        root = ElementTree.Element("book")
        title = ElementTree.SubElement(root, "title")
        title.text = book.title
        content = ElementTree.SubElement(root, "content")
        content.text = book.content
        return ElementTree.tostring(root, encoding="unicode")


SERIALIZE_MAP = {
    "json": JSONSerializeType,
    "xml": XMLSerializeType,
}
