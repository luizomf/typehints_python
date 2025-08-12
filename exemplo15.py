#
# Liskov Substitution Principle ou Princípio da substituição de Liskov
#
# Artigo: https://www.otaviomiranda.com.br/2025/liskov-substitution-principle-lsp-solid/
#
# Pré-condições: O subtipo não pode ser mais restritivo que o tipo base.
# Contravariância = C[A] <: C[B]
# Pós-condições: O subtipo não pode entregar menos do que o tipo base prometeu.
# Covariância = C[B] <: C[A]
# Invariantes: O subtipo deve manter todos os invariantes do tipo base.
# Invariância = C[A] != C[B]
#
from abc import ABC, abstractmethod

from utils import cyan_print, sep_print


class Shape(ABC):
    @property
    @abstractmethod
    def area(self) -> int: ...


class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        # Invariância: largura e altura são independentes
        self.width = width
        self.height = height

    @property
    def area(self) -> int:
        return self.width * self.height


class Square(Shape):
    def __init__(self, side: int) -> None:
        self._side = side

    @property
    def area(self) -> int:
        return self._side * self._side


def use_rectangle(r: Rectangle) -> None:
    r.width = 5
    r.height = 4

    cyan_print(f"{type(r).__name__}", r.width, r.height, r.area)

    assert r.area == 20, "Área incorreta..."


if __name__ == "__main__":
    rectangle = Rectangle(50, 40)
    square = Square(10)

    sep_print()

    use_rectangle(rectangle)
    use_rectangle(square)

    sep_print()
