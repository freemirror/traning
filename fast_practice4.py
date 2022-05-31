def cache3(func):
    count = {}
    cache = func()
    count[func] = 0
    def wrapper():
        if count[func] == 0:
            count[func] += 1
            return cache

        elif count[func] < 3:
            count[func] += 1
            return cache
        else:
            count[func] = 1
            return func()

    return wrapper


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())