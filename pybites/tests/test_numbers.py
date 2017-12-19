from mynumbers import sum_numbers
from names import clean_names, sort_by_surname_desc, shortest_name

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def test_sum():
    answer = 10
    assert sum_numbers([5,5]) == answer
    assert sum_numbers() == 5050

def test_shortest_name():
    assert shortest_name(NAMES) == 'Al'

def test_clean_names():
    result = clean_names(NAMES)
    assert isinstance(result, (list,))

def test_sort_by_surname_desc():
    result = sort_by_surname_desc(NAMES)
    assert result[-1] == 'Julian Sequeira'
    assert result[0] == 'Alec Baldwin'
    