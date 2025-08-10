#
# Genéricos padrão em Collections ABC
#
# Doc:
# Vídeo sobre protocolos: https://www.youtube.com/watch?v=8xnIkjROj_o
# https://docs.python.org/3/library/collections.abc.html
# https://docs.python.org/3/library/stdtypes.html#standard-generic-classes
#
# Como vimos antes, podemos usar as coleções padrão do Python para tipagem. Ou
# seja: `list[T]`, `dict[K, V]`, `tuple[T, ...]`, etc...
# Mas, isso deixa o meu código fixado no tipo escolhido. Uma função que recebe
# uma `list[str]` só pode receber `list[str]` e nada mais... E daí?
#
# Isso vai contra o Princípio da Robustez ou Lei de Postel, que diz:
#
# "Seja liberal no que você aceita, e conservador no que você retorna."
#
# Em resumo: para parâmetros que recebemos, devemos usar o tipo mais abstrato,
# enquanto nos retornos usamos valores mais restritos.
#
# Isso faz muito sentido quando você pensa em como um código funciona. Se uma
# função aceita algo que você pode percorrer (iterável), uma lista cumpre o
# papel, mas restringe todos os outros tipos que podem ser percorridos.
# Por outro lado, se uma função diz que vai retornar uma lista, o desenvolvedor
# que vai usar a função saberá os métodos que pode usar nessa lista sem quebrar
# o programa.
#
from collections.abc import Iterable

from utils import cyan_print, sep_print


def concat(items: Iterable[str]) -> str:
    return "".join(items)


letters_list = ["a", "b", "c"]
letters_set = {"a", "b", "c"}
letters_str = "abc"
letters_tuple = "a", "b", "c"
letters_dict = {"a": None, "b": False, "c": 123}

sep_print()

cyan_print(f"{concat(letters_list) = !r}")
cyan_print(f"{concat(letters_set) = !r}")
cyan_print(f"{concat(letters_str) = !r}")
cyan_print(f"{concat(letters_tuple) = !r}")
cyan_print(f"{concat(letters_dict) = !r}")

sep_print()
