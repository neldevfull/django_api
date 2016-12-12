"""

*** Jogo FizzBuzz ***

Regras
-------------------------------------------------------------------------------

- Quando a posição é múltipla de 3, fale fizz;
- Quando a posição é múltipla de 5, fale buzz;
- Quando a posição for múltipla de 3 e de 5, fale fizzbuzz;
- Para todas as outras existe mastercard, brincadeira, só fale o próximo número
"""


multiple_of = lambda base, num: num % base == 0


def robot(pos):
    fizz = 3
    buzz = 5
    result = str(pos)

    if (multiple_of(fizz, pos) and
            multiple_of(buzz, pos)):
        result = 'fizzbuzz'
    elif multiple_of(fizz, pos):
        result = 'fizz'
    elif multiple_of(buzz, pos):
        result = 'buzz'

    return result
