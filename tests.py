import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_init_dictionary_books_genre_is_exist_and_is_empty(self):
        collector = BooksCollector()

        assert collector.books_genre == {}
    
    def test_init_list_favorites_is_exist_and_is_empty(self):
        collector = BooksCollector()

        assert collector.favorites == []
    
    def test_init_list_genre_is_exist_and_correct(self):
        collector = BooksCollector()

        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_init_list_genre_age_rating_is_exist_and_correct(self):
        collector = BooksCollector()

        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_one_book_only_once(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1
    
    @pytest.mark.parametrize('name', ['','Очень длинное название книги, в котором больше чем 41 символ'])
    def test_add_new_book_name_short_or_long_length(self, name):
        collector = BooksCollector()
        book_not_added = collector.add_new_book(name)
        assert collector.get_books_genre() == {}

    def test_add_new_book_name_book_genre_is_empty_by_default(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
                
        assert collector.get_books_genre().get('Гордость и предубеждение и зомби') == ''

    def test_set_book_genre_genre_is_set(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        
        assert collector.get_books_genre().get('Гордость и предубеждение и зомби') in ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    @pytest.mark.parametrize('name, genre', [['Гордость и убеждение и зомби','Ужасы'],['Гордость и предубеждение и зомби','Ушассcы']])
    def test_set_book_genre_genre_is_not_set_if_Book_name_or_genre_is_not_exist(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre(name, genre)
        
        assert collector.get_books_genre().get('Гордость и предубеждение и зомби') == ''

    def test_get_book_genre_book_genre_return_as_added(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_list_of_books_with_specific_genre_not_empty(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби']
    
    def test_get_books_genre_get_dictionary_of_books_with_names_and_genres_correctly(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Фантастика')

        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби':'Ужасы', 'Что делать, если ваш кот хочет вас убить':'Фантастика'}

    def test_get_books_for_children_get_list_with_books_for_children_not_empty(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Фантастика')

        assert collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']

    def test_add_book_in_favorites_book_added(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.favorites == ['Что делать, если ваш кот хочет вас убить'] 

    def test_add_book_in_favorites_cant_add_book_if_book_not_in_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.favorites == [] 

    def test_delete_book_from_favorites_book_removed(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert collector.favorites == ['Что делать, если ваш кот хочет вас убить']
    
    def test_get_list_of_favorites_books_get_list_of_favorities_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']
        