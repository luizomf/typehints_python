from collections.abc import Sequence
from typing import TypeGuard, reveal_type

from utils import sep_print

################################################################################
#
# TypeGuard no Python: O Fiscal de Tipos Que Você NÃO Conhece 🚨 (Aula 16)
#
# `TypeGuard[T]` e `TypeIs[T]` são usados para "Type Narrowing" (afunilamento de tipo)
# no Python. Ambas fazem algo similar ao que já vimos com `isinstance()`, porém
# diferem nos argumentos de entrada e no contexto.
# `TypeGuard` funciona de uma forma contra intuitiva, enquanto `TypeIs` é bem
# mais tranquilo de ser utilizado.
#
################################################################################
#
# Obs.: As PEPs 742 e 647 falam sobre `TypeIs` e `TypeGuard`. Nessa aula vamos
# focar em `TypeGuard` e na próxima falamos sobre `TypeIs`.
#
################################################################################
#
# Uma forma bem simples de entender o que `TypeGuard[T]` e `TypeIs[T]` fazem é
# sempre imaginar cada um deles como `isinstance()` só que dentro da sua própria
# função, com seus argumentos e retorno de tipo. Depois é só entender as
# peculiaridades de cada um.
#
################################################################################
#
# Como `TypeGuard[T]` Funciona? (`T` sendo tipo target)
#
# - Usado para anotar o retorno de uma função de afunilamento de tipo (Type Predicate).
# - Se o retorno da função for `True`, o tipo é afunilado para `T`.
# - Se o retorno da função for `False`, explico mais abaixo em "IMPORTANTE".
# - Dá para enviar muitos args para a função, mas o primeiro é para o tipo de entrada.
# - O tipo do primeiro argumento pode não ter relação com `T`.
# -` TypeGuard[T]` PODE ser genérico (`T` pode ser dinâmico).
# - `TypeGuard[T]` aceita `Callable[..., T]` e Callback Protocol (que vimos antes).
#
################################################################################
#
# IMPORTANTE: `TypeGuard[T]` faz type "cast" permanente no caminho `True`. Por
# isso, ao analisar o código após o bloco `if/else`, o type checker precisa
# considerar as duas possibilidades que poderiam ter acontecido: o tipo original
# (se o caminho `False` foi seguido) e o novo tipo `T` (se o caminho `True` foi
# seguido). Por isso, ele cria uma Union para representar essa incerteza.
#
################################################################################


def is_list_str(values: Sequence[object]) -> TypeGuard[list[str]]:
    return all(isinstance(v, str) for v in values)


################################################################################


if __name__ == "__main__":
    sep_print()

    items1 = [22, "a"]
    if is_list_str(items1):
        reveal_type(items1)  # list[str] -> Comportamento esperando
    else:
        reveal_type(items1)  # list[str | int] -> Comportamento esperado

    # Fora do bloco condicional, o type checker não faz ideia se seu tipo é
    # `list[str]` ou `list[str | int]`. Para Ele agora existem dois caminhos
    # possíveis: `list[str]` ou `list[str | int]`. Isso é porque o `TypeGuard`
    # faz `cast` permanente após seu uso.

    # Aqui o tipo é a alteração permanente do TypeGuard ou o seu tipo
    reveal_type(items1)  # list[str] | list[str | int]

    sep_print()

################################################################################
