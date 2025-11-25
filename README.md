# qa\_python

1)test\_init\_dictionary\_books\_genre\_is\_exist\_and\_is\_empty - тестируем,что при создании объекта класса, конструктор создает атрибут books\_genre = {} (модуль \_\_init\_\_)

2)test\_init\_list\_favorites\_is\_exist\_and\_is\_empty - тестируем,что при создании объекта класса, конструктор создает атрибут favorites = \[] (модуль \_\_init\_\_)

3)test\_init\_list\_genre\_is\_exist\_and\_correct - тестируем,что при создании объекта класса, конструктор создает атрибут self.genre = \['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'] (модуль \_\_init\_\_)

4)test\_init\_list\_genre\_age\_rating\_is\_exist\_and\_correct - тестируем,что при создании объекта класса, конструктор создает атрибут self.genre\_age\_rating = \['Ужасы', 'Детективы'] (модуль \_\_init\_\_)

5)test\_add\_new\_book\_add\_two\_books - тестируем добавление книги, соответствующее условиям(длина названия больше 0 и меньше 41 символа) (модуль add\_new\_book)

6)test\_add\_new\_book\_add\_one\_book\_only\_once - тестируем,что одну книгу можно добавить долько один раз (модуль add\_new\_book)

7-9)test\_add\_new\_book\_name\_normal\_length - тестируем позитивные граничные значения длины названия книги при её добавлении(1;22;40) (модуль add\_new\_book)

10-13)test\_add\_new\_book\_name\_short\_or\_long\_length - тестируем негативные граничные значения длины названия книги при её добавлении(0;41;42;60) (модуль add\_new\_book)

14)test\_add\_new\_book\_name\_book\_genre\_is\_empty\_by\_default - тестируем, что при добавлении книги, жанр по умолчанию пустая строка (модуль add\_new\_book)

15)test\_set\_book\_genre\_genre\_is\_set - тестируем, что существующей книге можно назначить существующий жанр (модуль set\_book\_genre)

16-17)test\_set\_book\_genre\_genre\_is\_not\_set\_if\_Book\_name\_or\_genre\_is\_not\_exist - тестируем, что несуществующей книге нельзя назначить существующий жанр и наоборот (модуль set\_book\_genre)

18)test\_get\_book\_genre\_book\_genre\_return\_as\_added - тестируем, что возвращается тот же жанр, который мы добавили (модуль get\_book\_genre)

19)test\_get\_books\_with\_specific\_genre\_list\_of\_books\_with\_specific\_genre\_not\_empty - тестируем, что возвращается список книг с конкретным жанром (модуль get\_books\_with\_specific\_genre)

20)test\_get\_books\_genre\_get\_dictionary\_of\_books\_with\_names\_and\_genres\_correctly - тестируем, что корректно возвращается словарь books\_genre с добавленными в него ранее названиями и жанрами книг (модуль get\_books\_genre)

21)test\_get\_books\_for\_children\_get\_list\_with\_books\_for\_children\_not\_empty - тестируем, что возвращается список с названиями книг для детей (модуль get\_books\_for\_children)

22)test\_add\_book\_in\_favorites\_book\_added - тестируем, что книги добавляюся в избранное (модуль add\_book\_in\_favorites)

23)test\_add\_book\_in\_favorites\_cant\_add\_book\_if\_book\_not\_in\_books\_genre - тестируем,что в избранное нельзя добавить книгу,которая не была добавлена ранее в коллекцию книг (модуль add\_book\_in\_favorites)

24)test\_delete\_book\_from\_favorites\_book\_removed - тестируем,что книга удаляется из избранного (модуль delete\_book\_from\_favorites)

25)test\_get\_list\_of\_favorites\_books\_get\_list\_of\_favorities\_books - тестируем, что можно получить список избранных книг (модуль get\_list\_of\_favorites\_books)

