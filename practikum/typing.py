from typing import Optional
from typing import Union
from typing import Any
from typing import Sequence, Dict, List, Tuple, Set
from typing import Callable


def printer() -> None:
    print("Вызови меня!")


def returner(word: str) -> str:
    return word


def app(printed_inside: Callable[[], None], returned_inside: Callable[..., str]) -> None:
    printed_inside()
    print(returned_inside('Нет, вызови меня!')) 


def hundreds(х: Union[int, str]) -> str:
    return str(х * 100)

# Создан псевдоним для сложного типа данных:
CustomDict = Dict[str, List[Union[int, str]]]
# Указание того же типа для переменной (без псевдонима)
#def just_return_it(incoming: Dict[str, List[Union[int, str]]]) -> Dict[str, List[Union[int, str]]]:
#    return incoming

def just_return_it(incoming: CustomDict) -> CustomDict:
    return incoming

print(hundreds(100))
print(hundreds('сто'))
text: Optional[str]
var: str
var = None
text = None
print(var)
x: Any
x = 12210
x = 'Строка'
x = True
x = None
# Можно всё! Переменная x примет любой тип данных.
# Это множество может принять только целые числа
var_set: Set[int] = {1, 2, 3, 4, 5, 6,}
# Ключ аннотирован как строка, а значение - как целое число
var_dict: Dict[str, int] = {'forty_two': 42, 'hundred': 100,}
var_list: List[int] = [1, 2, 3, 4,]
var_tuple: Tuple[int, int, str, float] = (1, 2, 'привет', 1.618,)
# Многоточие (Ellipsis) - это указание для Python, что длина кортежа не определена
var_tuple: Tuple[float, ...] = (1, 2, 3.4,)
# Универсальный тип Sequence (Последовательность),
# подойдёт для аннотирования списка или множества

# <имя_переменной>: Sequence[<тип_всех_элементов>]
# принимает список
var_sequence: Sequence[float] = [1.2, 2, 3,]
# и принимает множество
var_sequence: Sequence[float] = {1.2, 2, 3,}
var_tuple: Tuple[Union[str, int, bool], ...] = (True, 13, 'наш кортеж',)
app(printer, returner)
app(printer, printer)
