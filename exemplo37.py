from dataclasses import dataclass
from typing import NewType, cast

from utils import cyan_print, sep_print

################################################################################
#
# NewType NÃO É genérico, nem TypeAlias
#
# Você não vai definir um NewType como genérico, mas poderia usar um
# genérico fixo como tipo base para seu NewType. (Te mostro no exemplo a seguir)
# No final, NewType é como se não fosse NADA para o runtime, porém é só um tipo
# para o Type Checker.

# Lembrando que NewType também NÃO É Type Alias:
# - TypeAlias = Aponta para um tipo complexo de escrever (como um atalho ou variável)
# - NewType = Gera um tipo distinto para o Type Checker apenas
#
################################################################################


# Um genérico de exemplo
@dataclass
class TheGeneric[T]:
    data: T


################################################################################

# Meus NewTypes usam genéricos com tipos fixos
# UsesGenericInt <: TheGeneric[int]
UsesGenericInt = NewType("UsesGenericInt", TheGeneric[int])
# UsesGenericStr <: TheGeneric[str]
UsesGenericStr = NewType("UsesGenericStr", TheGeneric[str])
# Union = Ou
NotGenericNT = UsesGenericInt | UsesGenericStr

################################################################################


# Uma função só para exemplo
def fn(not_generic_nt: NotGenericNT) -> NotGenericNT:
    # A checagem de tipo aqui é NO VALOR da minha dataclass
    if isinstance(not_generic_nt.data, str):
        print(f"{not_generic_nt.data} is str")
        return not_generic_nt

    print(f"{not_generic_nt.data} is int")
    return not_generic_nt


################################################################################


if __name__ == "__main__":
    sep_print()

    # Chamada meio confusa, mas é: str -> dataclass -> NewType -> fn
    value1 = fn(UsesGenericStr(TheGeneric("STR")))
    # Aqui é: int -> dataclass -> NewType -> fn
    value2 = fn(UsesGenericInt(TheGeneric(42)))

    # ⚠️⚠️⚠️ ATENÇÃO
    # O `cast` faz type cast de um tipo em outro quando você
    # tem certeza absoluta do tipo naquele ponto do código.
    # Observação: Fazer type cast forçado pode ser code smell.

    # Estou falando para o Pyright confiar em mim
    # pois sei o que estou fazendo.
    value2 = cast("TheGeneric[int]", value2)

    sep_print()

    # Para o Type Checker, NotGenericNT
    cyan_print(f"{value1.data=}")  # Para o Python é minha dataclass
    cyan_print(f"{value2.data=}")

    sep_print()

################################################################################
