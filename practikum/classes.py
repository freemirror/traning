class User:
    def __init__(self, name, phone, address, birthday):
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday

    def show(self):
        print(f'Имя: {self.name}, '
              f'адрес: {self.address}, '
              f'телефон: {self.phone}, '
              f'день рождения: {self.birthday}')

    def __str__(self):
        return f'Пользователь: {self.name}'


class Employee(User):
    def __init__(self, name, phone, address, birthday, employ_date):
        super().__init__(name, phone, address, birthday)
        self.employ_date = employ_date

    def show(self):
        print(f'Имя: {self.name} || дата трудоустройства: {self.employ_date}')


class Slave(User):
    def show(self):
        print(f'{self.name} работает за бесплатно')


def print_user_data(user):
    print(f"{user.name} - адрес: {user.address}, телефон: {user.phone},"
          f" день рождения: {user.birthday} ")


max = User(name='Макс',
           phone='+79854564411',
           address='Обнинск',
           birthday='09.11.1980')
gregory = User(name='Грегориан',
               phone='+79814445566',
               address='Балашиха',
               birthday='07.08.1992')
trevor = Employee(name='Тревор',
                  phone='+75554122188',
                  birthday='04.01.2000',
                  address='Смоленск',
                  employ_date='25.08.2021')
spartak = Slave(name='Спартак',
                phone='+5',
                birthday='06.10.0015',
                address='Рим')
max.show()
gregory.show()
print(max.phone)
print('\n Далее функции\n')
print_user_data(max)
print_user_data(gregory)
print('\n Опять методы классов\n')
print(max)
trevor.show()
spartak.show()
