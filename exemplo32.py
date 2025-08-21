################################################################################
#
# TypedDict - E chaves com nomes "inválidos"?
#
# Outra forma de criar `TypedDict` é com uma abordagem "funcional". Isso permite
# criar chaves com nomes inválidos, chaves que são keywords da gramática do
# Python ou até chaves com underlines (que seriam privadas na classe).
#
################################################################################


from typing import NotRequired, TypedDict

from utils import cyan_print, sep_print

NiceDict = TypedDict(
    "NiceDict",
    {
        "first-name": str,  # traço na chave
        "last-name": NotRequired[str],  # traço na chave
        "birth-year": int,  # traço na chave
        "in": NotRequired[bool],  # Keyword da gramática do Python
        "__it-works": str | None,  # Em classe isso faria name mangling (privado)
    },
)

if __name__ == "__main__":
    sep_print()

    nice_dict: NiceDict = {
        "first-name": "Otávio",
        "last-name": "Miranda",
        "birth-year": 2000,
        "in": False,
        "__it-works": None,
    }

    cyan_print(nice_dict["first-name"])
    cyan_print(nice_dict["last-name"])

    sep_print()


################################################################################
