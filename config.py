from ast import literal_eval
import re

def get_dimention():
    dim_regex = r'(?i)DIM\ *=\ *([0-9]*)\ *\n'

    dim_parsed = re.findall(dim_regex, file)
    if not dim_parsed:
        raise Exception("Parser", "Dimention not found")

    return int(dim_parsed[0])


def get_population():
    pop_regex = r'(?i)POP\ *=\ *([0-9]*)\ *\n'

    pop_parsed = re.findall(pop_regex, file)
    if not pop_parsed:
        raise Exception("Parser", "Population not found")

    return int(pop_parsed[0])


def get_codification():
    cod_regex = r'(?i)COD\ *=\ *([A-Za-z\_]+)(?:\ *(?:\ *-\ *bounds\ *)?\ *=?\ *\[(\ *-?[0-9]+\.?[0-9]*)\ *\,\ *-?([0-9]+\.?[0-9]*)\ *\])?\ *\n'

    cod_parsed = re.findall(cod_regex, file)
    if not cod_parsed:
        raise Exception("Parser", "Codification not found")

    key = str(cod_parsed[0][0])
    minC, maxC = None,None
    if cod_parsed[0][1]:
        minC = int(cod_parsed[0][1])
        maxC = int(cod_parsed[0][2])
    return key, minC, maxC


def parse(path: str):
    global file
    
    file = open(path, 'r').read()
    return dict(zip(
        ("population_size", "chromosome_size", "key", "min", "max"),
        (get_population(), get_dimention(), *get_codification())
    ))
