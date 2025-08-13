#
# TypeVar e funções genéricas no Python moderno - Aula 8
#
# Usaremos a nova sintaxe definida pela PEP 695 (Python >=3.12)
# https://docs.python.org/3/whatsnew/3.12.html#pep-695-type-parameter-syntax
#
# O modo anterior (que ainda pode ser usado) era definido com o seguinte:
#
# from typing import TypeVar
#
# 1. Unconstrained type variable (TypeVar livre)
# Pode ser substituído por qualquer tipo.
_T = TypeVar("_T")  # novo [T]
#
# 2. Bounded type variable (TypeVar com upper bound)
# Só pode ser substituído por `str` ou subtipos de `str`.
_U = TypeVar("_U", bound=str)  # novo [U: str]
#
# 3. Covariant type variable
# Usado em contextos de "produção" de valores (output),
# permite que subtipos sejam aceitos onde se espera o tipo base.
_V_co = TypeVar("_V_co", covariant=True)  # PEP 695: variância inferida no uso
#
# 4. Contravariant type variable
# Usado em contextos de "consumo" de valores (input),
# permite que supertipos sejam aceitos onde se espera o subtipo.
_W_contra = TypeVar("_W_contra", contravariant=True)  # PEP 695: variância inferida
#
# 5. Bounded type variable com união de tipos como bound
# Aceita apenas `str` ou `bytes` (ou subtipos de cada um).
_X = TypeVar("_X", bound=str | bytes)  # novo [X: str | bytes]
#
# 6. Constrained type variable (TypeVar com restrições explícitas)
# Pode ser apenas `int` ou `str` (tipos exatos ou subtipos deles).
_Y = TypeVar("_Y", int, str)  # novo [Y: (int, str)]
#
# 7. Default Type (TypeVar com tipo padrão)
# Se um tipo não for informado inicialmente, temos um tipo padrão `str`
_Z = TypeVar("_Z", default=str)  # novo [Z = str]

from collections.abc import Iterable, Sequence
from typing import TypeVar

from utils import cyan_print, sep_print

_T = TypeVar("_T")


def filter_by_type(items: Iterable[object], type_: type[_T]) -> list[_T]:
    return [item for item in items if isinstance(item, type_)]


def reverse_in_groups(items: Sequence[_T], group_size: int = 2) -> list[_T]:
    return [
        group
        for index in range(0, len(items), group_size)
        for group in reversed(items[index : index + group_size])
    ]


if __name__ == "__main__":
    sep_print()

    mixed = [1, 2, 3, "a", "b", "c", {10, 20}]
    # filtered: list[set[int]] = filter_by_type(mixed, set)
    # cyan_print(filtered)

    sep_print()

    reversed_groups = reverse_in_groups(mixed, group_size=4)
    cyan_print(mixed)
    cyan_print(reversed_groups)

    sep_print()
