import re
from typing import Protocol

from utils import cyan_print, sep_print

################################################################################
#
# TypeVar com callback protocol
#
# Também é possível usar `TypeVar` com protocols. Isso permite que você faça a
# assinatura da sua função de forma mais dinâmica. Assim, os tipos podem variar
# de acordo com o contexto.
# No exemplo abaixo, tenho um Protocol super simples. A intenção é receber sempre
# um atributo nomeado chamado `value` com tipo `T` e retornar `R`.
# Ambos `T` e `R` são `TypeVars` ou Type Parameters dinâmicos.
#
################################################################################

# Essa expressão regular será usada para limpar vírgulas.
# Ela seleciona o seguinte:
# - `\s*` - zero ou mais espaços
# - `,` - a vírgula
# - `\s*` - zero ou mais espaços
# Tenho curso grátis sobre isso aqui:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm1VnTa2Np5vDzCxVtyaYLMr
RE_COMMA_SPACE = re.compile(r"\s*,\s*")


################################################################################

# Vamos definir o nosso `Protocol` que aceita tipos parametrizados (`TypeVar`).


class TypeCaster[T, R](Protocol):
    def __call__(self, *, value: T) -> R: ...


################################################################################

# Agora podemos definir nossas funções que cumprem o contrato.


def to_str(*, value: object) -> str:
    """Recebe qualquer coisa e converte em string"""

    return str(value)


def str_to_list(*, value: str) -> list[str]:
    """Recebe uma string e tenta converter em lista"""

    clean_value = RE_COMMA_SPACE.sub(value, ",")
    return [v.strip() for v in RE_COMMA_SPACE.split(clean_value) if v.strip()]


def wrong_kw_name(text: str) -> str:
    """❌ Esse argumento nomeado está com nome errado"""

    return text


################################################################################

# Por fim vamos definir algo que "usa" o nosso `Protocol` e testamos se nossas
# funções passam na tipagem. Perceba que aqui estamos realmente usando as nossas
# funções como callback (fazendo o nome callback protocol valer).


def run_type_caster[T, R](value: T, type_caster: TypeCaster[T, R]) -> R:
    """Recebe um valor, um type_caster e executa tudo"""

    return type_caster(value=value)


################################################################################

# Bora testar tudo

if __name__ == "__main__":
    value_to_str = run_type_caster([1, 2, 3], to_str)
    value_to_list = run_type_caster(
        ",,,,abc,,,def,Luiz Otávio, a, b,c ,,,",
        str_to_list,
    )

    # Isso não só gera erro na tipagem, mas também no runtime
    # wrong_callback = run_type_caster("", wrong_kw_name)  # ❌

    # Aqui eu estou tentando enviar um `int` para um callback que espera `str`
    # Também gera erro tanto na tipagem quanto no runtime
    # wrong_argument = run_type_caster(123, str_to_list)  # ❌

    sep_print()

    cyan_print(f"{value_to_str = }")
    cyan_print(f"{value_to_list = }")
    # cyan_print(f"{wrong_kw_name = }")  # ❌
    # cyan_print(f"{wrong_argument = }")  # ❌

    sep_print()
