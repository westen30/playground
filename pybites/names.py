NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def clean_names(names):
    'dedup and title case names'
    names_set = set(names)

    return list(name.title() for name in names_set)


def sort_by_surname_desc(names):
    names = clean_names(names)

    return sorted(names, key=lambda x: x.split(" ")[-1], reverse=False)


def shortest_name(names):
    'name not surname'
    names = clean_names(names)
    return min(name.split(' ')[0] for name in names)
