import pytest
from main import  BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def collector_with_books_and_genres():
    collector = BooksCollector()
    collector.add_new_book('AHAHA')
    collector.set_book_genre('AHAHA', 'Ужасы')
    collector.add_new_book('OHOHO')
    collector.set_book_genre('OHOHO', 'Комедии')
    return collector