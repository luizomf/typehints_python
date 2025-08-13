#
# TypeVar e funções genéricas no Python moderno - Aula 8
#
# Usaremos a nova sintaxe definida pela PEP 695 (Python >=3.12)
# https://docs.python.org/3/whatsnew/3.12.html#pep-695-type-parameter-syntax
#
# Definições:
# `class Person[T]: ...` - O `T` significa "type parameter" ou "type variable"
# `Person[str]('John')` - O `str` entre colchete significa "type argument"
#
# Type variable (TypeVar) é um parâmetro de tipo que atua como um símbolo para
# um tipo ainda não conhecido. Seu valor será substituído por um tipo concreto
# durante a verificação estática ou inferência de tipos.
#
# Atualmente podemos usar os colchetes para definir uma TypeVar implicitamente.
# Com isso, não é mais necessário importar TypeVar e/ou Generic para definir um
# genérico parametrizado.
#
# DOC: NÃO MISTURAR A VERSÃO NOVA COM A VERSÃO ANTIGA NOS SEUS TIPOS.
#

from collections.abc import Hashable, MutableMapping

from utils import cyan_print, sep_print


# O hash do dicionário é um número calculado pelo __hash__ que serve como
# identificador rápido do conteúdo de algumas estruturas de dados como
# dict e set.
# O hash nunca deve mudar, por isso os valores para a chave precisam ser imutáveis.
def invert_mapping[K, V: Hashable](m: MutableMapping[K, V]) -> MutableMapping[V, K]:
    return {value: key for key, value in m.items()}


if __name__ == "__main__":
    sep_print()

    dict1 = {
        "a": 1,
        "b": 2,
        (1, 2): 3,
    }
    invert = invert_mapping(dict1)
    revert = invert_mapping(invert)

    cyan_print(dict1)
    cyan_print(invert)
    cyan_print(revert)

    sep_print()
