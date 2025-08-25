from collections.abc import Sequence
from typing import TypeGuard, TypeIs, reveal_type

from utils import sep_print

################################################################################
#
# TypeGuard vs TypeIs no Python: Você PRECISA Aprender Urgente! (Aula 16)
#
# Exemplo REAL em TypeScript:
# https://www.youtube.com/watch?v=TaMvD9UmYVI
# https://github.com/luizomf/tests-nextjs-vitest-playwright/blob/main/src/env/configs.ts
#
################################################################################
#
# `TypeGuard[T]` e `TypeIs[T]` são utilitários de tipo do Python usados para
# gerar funções de "Type Narrowing" definidas pelo próprio desenvolvedor.
# Ambos fazem algo similar ao que já vimos com `isinstance()`, porém, como
# definimos a nossa própria função de "Type Predicate", podemos fazer várias
# checagens de tipo, valor, chave ou o que quer que precise checar para
# afunilar um tipo qualquer.
# Além disso, geramos funções que podem ser reaproveitadas ao longo do código.
#
# Obs.: As PEPs 742 e 647 falam sobre `TypeIs` e `TypeGuard`.
#
################################################################################
#
# Como `TypeGuard[T]` Funciona?
#
# - Usado para anotar o retorno de uma função de afunilamento de tipo (Type Predicate).
# - Deve retornar `bool` em todos os caminhos condicionais.
# - Permite múltiplos argumentos na função; mas o primeiro é o tipo de entrada.
# - Pode ser genérico (receber tipos parametrizados).
# - Pode trabalhar com Callable e Callback Protocol se quiser.
# - Pode ser usado como método de classe, basta incluir `self` (o resto é igual).
# - NÃO LIGA COM A CONSISTÊNCIA ENTRE O TIPO DO RETORNO E O TIPO DO PRIMEIRO ARGUMENTO.
# - SÓ INFERE PARA O CAMINHO POSITIVO (VERDADEIRO).
# - NO CAMINHO NEGATIVO (FALSO) NÃO INFERE NADA.
# - NÃO USA INFORMAÇÕES JÁ INFERIDAS, USA O TIPO EXATO.
#
################################################################################
#
# Como `TypeIs[T]` Funciona?
#
# - Anota o retorno de uma função de afunilamento de tipo (Type Narrowing Function).
# - Deve retornar `bool` em todos os caminhos condicionais.
# - Permite múltiplos argumentos na função; mas o primeiro é o tipo de entrada.
# - Pode ser genérico (receber tipos parametrizados).
# - Pode trabalhar com Callable e Callback Protocol se quiser.
# - Pode ser usado como método de classe, basta incluir `self` (o resto é igual).
# - O TIPO DO RETORNO DEVE SER CONSISTENTE COM O TIPO DO PRIMEIRO ARGUMENTO.
# - FUNCIONA TANTO PARA O CAMINHO POSITIVO QUANDO PARA O NEGATIVO (if e else).
# - USA INFORMAÇÕES JÁ INFERIDAS PARA UM TIPO MAIS PRECISO.

# Na teoria dos tipos isso é MUITO USADO (então só lembrando conjuntos):
#
# A∨R ou A | R - Union (Significa "OU")
# - Representa todos os valores que pertencem a A ou a R (ou a ambos).
# A∧R ou A & R - Intersection (Significa "E")
# - Representa todos os valores que pertencem a A e também a R.
# A∧¬R ou A & !R - Interseção com complemento (Significa "E NÃO")
# - Representa os valores que estão em A mas não em R (tipo .difference() dos sets).
#
# Relaxa que vou te explicar isso, só teoria rapidinho (você não vai nem sentir):
#
# - No caminho positivo, o tipo deve afunilado para A∧R (interseção entre A e R)
# - No caminho negativo, o tipo deve afunilado para A∧¬R (A e não R, ou A)
#
################################################################################


def is_list_str_guard(values: Sequence[object]) -> TypeGuard[list[str]]:
    has_str_only = [isinstance(v, str) for v in values]
    return all(has_str_only)  # all retorna `True` se tudo no iterável for `Truthy`


def is_list_str_is(values: Sequence[object]) -> TypeIs[list[str]]:
    has_str_only = [isinstance(v, str) for v in values]
    return all(has_str_only)


################################################################################


if __name__ == "__main__":
    sep_print()

    items_guard = [22, "b"]
    # items_guard = ["a", "b"]
    if is_list_str_guard(items_guard):
        # Pyright: list[str].
        # MyPy: builtins.list[builtins.str].
        # Mesmo comportamento.
        reveal_type(items_guard)
    else:
        # ESTE CAMINHO NÃO É AFETADO PELO TYPEGUARD.
        # Pyright: list[str | int].
        # MyPy: builtins.list[builtins.object].
        # Aqui o comportamento tá bem estranho no MyPy.
        # Prefiro a forma do PyRight, é mais intuitivo.
        reveal_type(items_guard)

    # Quando usamos TypeGuard, isso geralmente acontece fora do bloco condicional.
    # Os Type Checkers simplesmente não sabem mais qual o tipo do objeto.

    # Pyright: list[str] | list[str | int]
    # MyPy: builtins.list[builtins.object]

    # Comportamento estranho de novo, parece que todo mundo "CHUTOU" o tipo.
    # Isso é porque não entramos no "Happy Path" e ao chamar Type Predicate
    # o tipo receber uma tagzinha de nova possibilidade de tipo.
    reveal_type(items_guard)

    sep_print()

    ################################################################################

    items_is = [22, "b"]
    # items_is = ["a", "b"]
    if is_list_str_is(items_is):
        # Pyright: Never - Ele sabe que não virá aqui por que está vendo os tipos
        # MyPy: builtins.list[builtins.str].
        reveal_type(items_is)
    else:
        # Pyright: list[str | int] - Eu gosto desse comportamento (é o mesmo tipo)
        # MyPy: Nem falou nada disso aqui
        reveal_type(items_is)

    # Pra mim tá tudo normal aqui agora (TypeIs é mais seguro e intuitivo)
    # Mas de novo, cada um fala uma coisa.

    # Pyright: list[str | int]
    # MyPy: builtins.list[builtins.str]

    # Comportamento estranho de novo, parece que todo mundo "CHUTOU" o tipo.
    # Isso é porque não entramos no "Happy Path" e ao chamar Type Predicate
    # o tipo receber uma tagzinha de nova possibilidade de tipo.
    reveal_type(items_is)

    sep_print()

################################################################################
