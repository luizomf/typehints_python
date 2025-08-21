################################################################################
#
# TypedDict - Subtipagem para composição
#
# É possível usar subtipagem para compor outros `TypedDicts` com mais campos.
# Por exemplo, um `TypedDict` `A` pode ter a chave `a` e outro `B` a chave `b`.
# Se `B` herdar de `A`, `B` terá as chaves `a` e `b`.
# Prefira vários `TypedDicts` pequenos (ex.: UserBase, UserContact) e compor
# no código.
#
#
################################################################################


from typing import TypedDict

from utils import cyan_print, sep_print


class Colored(TypedDict):
    background: str
    foreground: str


class Sized(TypedDict):
    width: int
    height: int


class Rectangle(Sized, Colored): ...


if __name__ == "__main__":
    sep_print()

    rectangle: Rectangle = {
        "background": "black",
        "foreground": "white",
        "width": 5,
        "height": 5,
    }

    cyan_print(rectangle["background"])
    cyan_print(rectangle["foreground"])
    cyan_print(rectangle["width"])
    cyan_print(rectangle["height"])

    sep_print()

################################################################################
