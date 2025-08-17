#
# ABC vs Protocol
#
# Protocol é bem parecido com ABC, mas há diferenças que mudam a escolha:
#
# ABCs → Contrato nominal com efeito em runtime. Você precisa herdar da ABC;
# classes que não implementam os abstratos não instanciam. Além disso,
# isinstance/issubclass funcionam normalmente.
#
# Protocols → Contrato estrutural pensado pro type checker. Você não precisa
# herdar: basta ter a forma certa (métodos/atributos compatíveis).
# Em runtime, Protocol não valida implementações por conta própria. Se quiser
# checar em runtime, use @runtime_checkable, ele só verifica se o atributo existe,
# não se a assinatura bate 100%.
#
# Regrinha mental:
# - Precisa impor regra em runtime via herança? → ABC.
# - Quer aceitar quem tem a forma certa sem acoplamento nominal? → Protocol.
#
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

from utils import cyan_print, sep_print


class ShapeAbc(ABC):
    @property
    @abstractmethod
    def area(self) -> float: ...


@runtime_checkable
class ShapeProtocol(Protocol):
    # Em Protocol não precisa de @abstractmethod; o checker já trata como contrato.
    @property
    def area(self) -> float: ...


class MyShapeAbc(ShapeAbc):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @property
    def area(self) -> float:
        return self.x * self.y


class MyShapeProtocol:
    @property
    def area(self) -> float:
        return 1.1


def wants_shape_abc(shape: ShapeAbc) -> None:
    cyan_print(shape.area)


def wants_shape_protocol(shape: ShapeProtocol) -> None:
    cyan_print(shape.area)


if __name__ == "__main__":
    sep_print()

    myshape_abc = MyShapeAbc(10, 20)
    myshape_protocol = MyShapeProtocol()

    wants_shape_abc(myshape_abc)
    # wants_shape_abc(myshape_protocol)  # ❌ precisa herdar de ShapeAbc

    wants_shape_protocol(myshape_abc)  # ✅ bate por estrutura (tem .area -> float)
    wants_shape_protocol(myshape_protocol)  # ✅ idem

    sep_print()
