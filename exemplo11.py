#
# Contravariância em genéricos padrão
#
# Doc: https://docs.python.org/3/library/collections.abc.html
#
# Um dos exemplos mais claros e fáceis de entender sobre contravariância no
# Python é o `Callable` (vimos em aulas anteriores).
# Ele é contravariante nos parâmetros de entrada e covariante no valor de
# retorno, exatamente como define a regra de variância.
#
# Aqui uso os termos "input" e "output" para facilitar a associação com outras
# linguagens: em Kotlin e C#, por exemplo, esses conceitos aparecem como
# `in` (contravariante) e `out` (covariante); já em Scala a notação é com sinais:
# `+T` para covariância e `-T` para contravariância.

from collections.abc import Callable


class Animal: ...


class Dog(Animal): ...


class Pitbull(Dog): ...


# Pitbull <: Dog <: Animal
# Imagine que temos funções especializadas em lidar com esses tipos:


def handle_pitbull(pitbull: Pitbull) -> None: ...
def handle_dog(dog: Dog) -> None: ...
def handle_animal(animal: Animal) -> None: ...


# Queremos uma função que receba um "handler" de Dog.
# No typing, Callable é contravariante nos parâmetros de entrada.
# Regra: se Dog <: Animal, então
# Callable[[Animal], None] <: Callable[[Dog], None]
def handle(handler: Callable[[Dog], None]) -> None: ...


# Isso pode parecer estranho de primeira, mas pense assim:
# Eu preciso de um especialista em cuidar de cachorros.
# Alguém que é especialista em cuidar de QUALQUER animal
# com certeza consegue cuidar de cachorros também.

# Para quem já é mais avançado:
# Eu preciso de algo que tenha o método .eat().
# Um supertipo de Dog também tem esse método .eat().
# É isso que a contravariância garante.

# Testando:
handle(handle_dog)  # ok
handle(handle_animal)  # ok

# Mas se eu preciso de um especialista em cachorros,
# um especialista só em Pitbull NÃO serve.
# Ele não saberia cuidar de um Fila, por exemplo.
handle(handle_pitbull)  # erro no type checker
