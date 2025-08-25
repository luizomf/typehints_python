import json
from pathlib import Path
from typing import Any, TypedDict, TypeGuard, cast

from utils import cyan_print, red_print, sep_print

################################################################################
#
# TypeGuard vs TypeIs - Quando usar cada um?
#
# A PEP 742 afirma explicitamente (tradução livre):
#
# "TypeIs é o sucessor espiritual da especificação original do TypeGuard, e nós
# esperamos que ele seja a escolha correta para a vasta maioria dos casos de uso."
#
################################################################################
#
# - Se só me importa o happy path -> TypeGuard.
# - Se quero narrowing confiável nos dois lados -> TypeIs.
# - Se o predicado pode transformar "um nada a ver" em outro tipo -> TypeGuard.
# - Se quero consistência entre input/output -> TypeIs.
#
################################################################################
#
# Atenção: é bom ter bastante certeza que sua função de análise faça a checagem
# de TODOS OS CAMINHOS POSSÍVEIS. Se enganarmos o Type Checker, estaremos nos enganando
# também. O "cast" é permanente para o Type Checker.
#
################################################################################


class UserDict(TypedDict):
    firstname: str
    lastname: str
    age: int


def is_valid_dict(item: object) -> TypeGuard[UserDict]:
    if not isinstance(item, dict):
        return False

    item = cast("dict[Any, Any]", item)  # isso é para o Pyright para de amolar

    if not isinstance(item.get("firstname"), str):
        return False

    if not isinstance(item.get("lastname"), str):
        return False

    return isinstance(item.get("age"), int)


################################################################################


if __name__ == "__main__":
    sep_print()

    input_file = Path("exemplo39.json").resolve()
    with input_file.open("r", encoding="utf8") as file:
        user_data = json.load(file)  # Any

    for user in user_data:
        if is_valid_dict(user):
            cyan_print("✅ VALID USER")
            cyan_print(f"{user['firstname']} {user['lastname']} {user['age']}")
        else:
            red_print("❌ INVALID DATA ❌")
            red_print(user)

    sep_print()

################################################################################
