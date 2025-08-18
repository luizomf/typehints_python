#
# Composição de Protocolos em Python: do ISP à tipagem estrutural
#
# Você pode compor protocolos como "blocos de lego", ou seja, é possível criar
# vários protocolos pequenos, com comportamento único e depois unir esse
# protocolos em algo maior. Este é um caso interessante para aderir ao Interface
# segregation principle (ISP) do SOLID.
#
# Regrinhas (Protocols em Python):
# - Herdar de QUALQUER Protocol (sem `Protocol` na lista) cria uma classe CONCRETA.
# - Herdar de um Protocol e incluir `Protocol` na lista, cria um NOVO Protocol composto.
# - Não precisa herdar de `Protocol` para ter tipagem estrutural (mas facilita).
# - @runtime_checkable (ABAIXO)
# - Atributos em Protocols são invariantes (mutáveis não variam), prefira @property
# - Protocols podem ser genéricos: `Protocol[T]`, contratos que variam com o tipo.
# - Composição de Protocols = herança múltipla, soma de contratos (bom pro ISP).
# - Ótimos para argumentos de métodos e funções (vamos falar disso depois).
#
# ⚠️ Atenção:
# Usar isinstance() com Protocols não é totalmente seguro em tempo
# de execução. Por exemplo, as assinaturas dos métodos não são verificadas.
# A checagem em runtime só garante que os membros do protocolo existem, não que
# eles têm o tipo certo. Já o issubclass() com Protocols também só confere se
# os métodos existem, nada além disso.
# https://typing.python.org/en/latest/reference/protocols.html#using-isinstance-with-protocols
#
# SOLID
# [S]ingle Responsibility Principle (SRP): uma classe deve ter apenas uma razão
#     para mudar.
# [O]pen/Closed Principle (OCP): entidades de software devem estar abertas para
#     extensão, mas fechadas para modificação.
# [L]iskov Substitution Principle (LSP): objetos de uma classe derivada devem
#     poder substituir objetos da classe base sem quebrar o programa.
# [I]nterface Segregation Principle (ISP): é melhor ter várias interfaces
#     específicas do que uma única interface geral.
# [D]ependency Inversion Principle (DIP): dependa de abstrações, não de
#     implementações.
#

import json
from collections.abc import Callable
from pathlib import Path
from typing import Protocol

from utils import cyan_print, sep_print


class SupportsRead[Out](Protocol):
    def read(self) -> Out: ...


class SupportsWrite[In](Protocol):
    def write(self, data: In) -> None: ...


class SupportsReadWrite[In, Out](SupportsRead[Out], SupportsWrite[In], Protocol): ...


class FileDataManager[Out](SupportsReadWrite[str, Out]):
    def __init__(self, path: Path, parser: Callable[[str], Out]) -> None:
        self.path = path
        self.parser = parser

    def read(self) -> Out:
        with self.path.open("r", encoding="utf-8") as file:
            data = file.read()

        return self.parser(data)

    def write(self, data: str) -> None:
        with self.path.open("w", encoding="utf-8") as file:
            file.write(data)


def manage_file[Out](file_manager: SupportsReadWrite[str, Out], data: str) -> Out:
    file_manager.write(data)
    return file_manager.read()


if __name__ == "__main__":
    sep_print()

    # Parser simples para int
    file_manager = FileDataManager(Path("./exemplo26_a.txt"), int)
    data = manage_file(file_manager, "123")
    cyan_print(data, type(data))  # 123, <class 'int'>

    # Parser JSON para list[int]
    file_manager = FileDataManager[list[int]](Path("./exemplo26_a.txt"), json.loads)
    data = manage_file(
        file_manager,
        "[1, 2, 3, 4]",  # ⚠️ string JSON, não Python literal
    )
    cyan_print(data, type(data))  # [1, 2, 3, 4], <class 'list'>

    # Parser JSON para dict[str, int]
    file_manager = FileDataManager[dict[str, int]](
        Path("./exemplo26_a.txt"),
        json.loads,
    )
    data = manage_file(file_manager, '{"a": 1, "b": 2}')
    cyan_print(data, type(data))  # {'a': 1, 'b': 2}, <class 'dict'>

    sep_print()
