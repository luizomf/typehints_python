#
# Para Type Checkers (Código não executado):
#
# Classes criam tipos. Assim como criamos `Animal` porque não encontramos um
# `Animal` pronto no Python, para o Type Checker, ao criar um `Animal`, você
# acabou de criar um novo tipo na linguagem chamado `Animal`. Esse tipo de
# tipagem é chamado de "Tipagem nominal" ou "Nominal typing".
# Todas as instâncias de animal são DO TIPO `Animal`.
# Se eu criar uma função que precisa receber um `Animal` (do exemplo anterior),
# `dog` ou `cat` vão servir.
# É por conta da tipagem nominal que quando precisamos de algo muito amplo,
# usamos `object`. A frase "em Python tudo é um objeto" confirma isso.
#

from exemplo05 import Animal
from utils import cyan_print, sep_print


def get_animal_name(animal: Animal) -> None:
    cyan_print(f"'get_animal_name' | Classe: {type(animal).__name__}")
    cyan_print(f"'get_animal_name' | {animal.name = !r}")
    sep_print()


if __name__ == "__main__":
    # Para os type checkers:
    dog = Animal("Dog")  # dog É UM Animal
    cat = Animal("Cat")  # cat É UM Animal

    sep_print()
    # Então abaixo função aceitaria qual tipo?
    get_animal_name(dog)  # Dog
    get_animal_name(cat)  # Cat
