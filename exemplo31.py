################################################################################
#
# TypedDict - Dicionários sem tipagem NUNCA MAIS
#
# Adicionar tipagem em dicionários sempre foi um desafio no Python. Isso
# acontece porque quanto mais você tenta deixar a tipagem de `dict` específica,
# mais combinações possíveis aparecem. Veja o exemplo:
#
# `mydict: dict[A | B, C | D] = {...}`
#
# Aqui você gerou 4 combinações possíveis de par (produto cartesiano):
# A=C, A=D, B=C, B=D.
# E você já pode perceber que, quanto mais chaves ou valores com `Union`, mais
# combinações possíveis.
#
# `dict` é ótimo para casos simples, onde não importa relacionar uma chave
# específica a um valor específico. Mas quando precisamos modelar um mapeamento
# fixo (chaves conhecidas, cada uma com seu tipo de valor), `dict` não resolve.
#
# Para esse cenário, usamos `TypedDict`.
#
# Veja alguns genéricos que podemos usar em conjunto com `TypedDict`:
#
# total: bool (default True): todas as chaves devem ou não estarem presentes.
# Required[T]: essa chave é requerida.
# NotRequired[T]: essa chave pode não existir, mas se vier tem que ser tipo `T`.
# T | None: esse Union indica que essa chave é opcional (existe mas pode ser None)
# Readonly: a chave não deve ser alterada
#
# Observação: em runtime isso é um dicionário normal. Nada da tipagem faz
# checagem em runtime.
#
#
################################################################################

from typing import NotRequired, ReadOnly, Required, TypedDict

from utils import cyan_print, sep_print


class MyDict(TypedDict, total=True):  # total=False: chaves podem faltar (default True)
    id: int
    name: str  # Required aqui seria redundante (total True)
    email: Required[str]
    gender: NotRequired[str]  # Isso pode ser confuso, a chave pode faltar
    birth: Required[ReadOnly[str | None]]


if __name__ == "__main__":
    sep_print()

    my_dict: MyDict = {
        "id": 1,
        "name": "Otávio Miranda",
        "email": "email@email.com",
        "gender": "masculino",  # NotRequired
        "birth": None,  # Opcional
    }

    cyan_print(my_dict["id"])
    cyan_print(my_dict["birth"])
    cyan_print(my_dict["gender"])

    sep_print()

    # Isso pode ser confuso, mas abaixo estou criando um dicionário
    # não é uma instância de classe. Não tem como acessar chaves pelo ponto.
    my_dict2 = MyDict(id=2312312, name="Luiz", email="email2@email.com", birth=None)
    # my_dict2["id"] = 23 # read-only

    cyan_print(my_dict2["id"])

    sep_print()

################################################################################
