from ast import literal_eval
import re


def get_dimention() -> dict:
    dim_regex = r'(?i)DIM\ *=\ *([0-9]*)\ *\n'

    dim_parsed = re.findall(dim_regex, file)
    if not dim_parsed:
        raise Exception("Parser", "Dimention not found")

    return dict(chromosome_size=int(dim_parsed[0]))


def get_population() -> dict:
    pop_regex = r'(?i)POP\ *=\ *([0-9]*)\ *\n'

    pop_parsed = re.findall(pop_regex, file)
    if not pop_parsed:
        raise Exception("Parser", "Population not found")

    return dict(population_size=int(pop_parsed[0]))


def get_cicles() -> dict:
    run_regex = r'(?i)RUN\ *=\ *([0-9]*)\ *\n'

    run_parsed = re.findall(run_regex, file)
    if not run_parsed:
        raise Exception("Parser", "RUN not found")

    return dict(cicles=int(run_parsed[0]))


def get_codification() -> dict:
    cod_regex = r'(?i)COD\ *=\ *([A-Za-z\_]+)(?:\ *(?:\ *-\ *bounds\ *)?\ *=?\ *\[(\ *-?[0-9]+\.?[0-9]*)\ *\,\ *-?([0-9]+\.?[0-9]*)\ *\])?\ *\n'

    cod_parsed = re.findall(cod_regex, file)
    if not cod_parsed:
        raise Exception("Parser", "Codification not found")

    key = str(cod_parsed[0][0])
    min, max = None, None
    if cod_parsed[0][1]:
        min = int(cod_parsed[0][1])
        max = int(cod_parsed[0][2])
    return dict(key=key, min=min, max=max)


def parse(path: str) -> dict:
    global file

    file = open(path, 'r').read()
    return dict(
        **get_dimention(),
        **get_population(),
        **get_cicles(),
        **get_codification()
    )
