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


def main():
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'


if __name__ == '__main__':
    main()
