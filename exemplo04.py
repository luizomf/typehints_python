#
# O que é um "Callable" em Python?
# De forma simples, "callable" é qualquer coisa que pode ser "chamada", ou
# seja, executada usando parênteses `()`.
#
# Os exemplos mais comuns são:
#   - Funções (que criamos com `def`)
#   - Métodos (funções dentro de classes)
#   - As próprias Classes (para criar instâncias `MinhaClasse()`)
#   - Objetos que implementam o método especial `__call__`
#
# Descrevendo Assinaturas com `collection.abc.Callable`
#
# Além de tipar os parâmetros e o retorno de uma função, às vezes precisamos
# dizer que uma variável ou um parâmetro é, ele mesmo, "do tipo função".
#
# Isso é muito comum em cenários mais avançados, como em decoradores ou em
# funções que recebem outras funções como argumento (conhecidas como
# "Higher-Order Functions" ou "HOF").
#
# Para esses casos, usamos o tipo especial `Callable` do módulo `collections.abc`.
# Ele nos permite criar um "contrato" ou uma "etiqueta" que descreve
# qual tipo de função esperamos receber.
#
# Agora, vamos ver tudo isso na prática!
#

from collections.abc import Callable

from utils import cyan_print, sep_print

sep_print()


def with_callback(
    x: float, y: float, callback: Callable[[str, str, bool], None]
) -> float:
    result = x + y
    callback(f"{result = }", "Another value", True)
    return x + y


def callback(text: str, another_text: str, example: bool = False) -> None:
    cyan_print(text, another_text, example)


with_callback(2, 5, callback)
sep_print()


def with_args(*args: str) -> None:
    cyan_print(*args)


with_args("with_args", "a", "b", "c")
sep_print()


def with_kwargs(*args: int, **kwargs: str) -> None:
    cyan_print("Args:", *args)
    cyan_print("Kwargs:", **kwargs)  # Desempacotar aqui vai dar problema
    # print("Kwargs:", **kwargs)  # Desempacotar aqui vai dar problema


with_kwargs(1, 2, 3, nome="Luiz", sobrenome="Otávio")
sep_print()
