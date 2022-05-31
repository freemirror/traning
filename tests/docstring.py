def movie_quotes(name):
    """Возвращает цитаты известных персонажей из фильмов

    >>> movie_quotes('Элли')
    'Тото, у меня такое ощущение, что мы не в Канзасе!'

    >>> movie_quotes('Шерлок')
    'Элементарно, Ватсон!'

    >>> movie_quotes('Дарт Вейдер')
    'Люк, я — твой отец.'

    >>> movie_quotes('Леонид Тощев')
    'Персонаж пока не известен миллионам.'
    """
    quotes = {
        'Элли': 'Тото, у меня такое ощущение, что мы не в Канзасе!',
        'Шерлок': 'Элементарно, Ватсон!',
        'Дарт Вейдер': 'Люк, я — твой отец.',
        'Thomas A. Anderson': 'Меня. Зовут. Нео!',
    }
    return quotes.get(name, 'Персонаж пока не известен миллионам.')


print(movie_quotes('Элли'))
print(movie_quotes('Шерлок'))
print(movie_quotes('Дарт Вейдер'))
print(movie_quotes('Леонид Тощев'))
print(movie_quotes.__doc__)


if __name__ == '__main__':
    import doctest
    doctest.testmod()