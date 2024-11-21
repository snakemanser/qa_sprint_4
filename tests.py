import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1 дефолтный список жанров создается правильно
    def test_default_value_genres_true(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    # 2 новая книга добавляется
    @pytest.mark.parametrize('name',[
        'AHAHA',
        'OHOHO'])
    def test_add_new_book_add_one_book(self, name, collector):
        collector.add_new_book(name)
        assert {name: ''} == collector.books_genre

    # 3 жанр устанавливается
    def test_set_book_genre_set_genre(self, collector):
        collector.add_new_book('AHAHA')
        collector.set_book_genre('AHAHA', 'Ужасы')
        assert 'Ужасы' == collector.books_genre['AHAHA']

    # 4 возвращается жанр книги по ее названию
    def test_get_book_genre_get_genre(self, collector_with_books_and_genres):
        assert 'Комедии' == collector_with_books_and_genres.get_book_genre('OHOHO')

    # 5 возвращается список с книгами определенного жанра
    def test_get_books_with_specific_genre_get_two_books(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_new_book('Как закерить 1х9')
        collector_with_books_and_genres.set_book_genre('Как закерить 1х9', 'Комедии')
        assert collector_with_books_and_genres.get_books_with_specific_genre('Комедии') == ['OHOHO', 'Как закерить 1х9']

    # 6 метод, который возвращает словарь, действительно возвращает словарь
    def test_get_books_genre_get_dict(self, collector_with_books_and_genres):
        assert collector_with_books_and_genres.books_genre == collector_with_books_and_genres.get_books_genre()

    # 7 создан список без фильма с жанром для возрастного рейтинга
    def test_get_books_for_children_create_list_without_genre_from_age_rating(self, collector_with_books_and_genres):
        assert 'AHAHA' not in collector_with_books_and_genres.get_books_for_children() and 'OHOHO' in collector_with_books_and_genres.get_books_for_children()

    # 8 если книга уже есть в избранном, то список избранного остается без изменений
    def test_add_book_in_favorites_not_added_bcs_already_in_favorites(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_book_in_favorites('AHAHA')
        collector_with_books_and_genres.add_book_in_favorites('AHAHA')
        assert len(collector_with_books_and_genres.favorites) == 1 and 'AHAHA' in collector_with_books_and_genres.favorites

    # 9 книга удаляется из избранного
    def test_delete_book_from_favorites_delete_one_book(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_book_in_favorites('AHAHA')
        collector_with_books_and_genres.delete_book_from_favorites('AHAHA')
        assert [] == collector_with_books_and_genres.favorites

    # 10 метод, который возвращает избранное, возвращает избранное
    def test_get_list_of_favorites_books_get_list(self, collector_with_books_and_genres):
        collector_with_books_and_genres.add_book_in_favorites('AHAHA')
        collector_with_books_and_genres.add_book_in_favorites('OHOHO')
        assert ['AHAHA','OHOHO'] == collector_with_books_and_genres.get_list_of_favorites_books()

