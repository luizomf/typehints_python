from dataclasses import dataclass
from typing import NewType

from utils import cyan_print, sep_print

################################################################################
#
# O que NewType É e NÃO É?
#
# Em runtime NewType SEMPRE será o tipo base do VALOR. Então você NÃO está
# criando uma nova classe ou subclasse, você está usando o TIPO DO VALOR usado.
# Para o Type Checker a história é diferente, ele considera NewType sempre sendo
# uma subclasse da classe base.
# Vamos simplificar isso com código.
#
################################################################################


# Essa dataclass será para meu exemplo
@dataclass
class PostId:
    value: str


# Esse NewType usa minha datatclass
StrPostId = NewType("StrPostId", PostId)


################################################################################


def get_post(post_id: StrPostId) -> StrPostId:
    return post_id


################################################################################


if __name__ == "__main__":
    sep_print()

    post_id = PostId("abcde")  # meu valor é do tipo correto (PostId)
    str_post_id = StrPostId(post_id)  # Isso é valido para o Type Checker (PostId)

    # Isso não é válido para o Type Checker e gera uma str no runtime
    this_is_a_string = "ABC"  # Perceba que o TIPO DO VALOR é str
    unexpected = StrPostId(this_is_a_string)  # Então isso gera uma str no runtime

    cyan_print(f"{post_id=}", type(post_id))  # ✅ Runtime: PostId
    cyan_print(f"{str_post_id=}", type(str_post_id))  # ✅ Runtime: PostId
    cyan_print(f"{unexpected=}", type(unexpected))  # ✅ Runtime: str

    sep_print()

################################################################################
