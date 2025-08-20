#
# Herança com protocolos (Só para constar no seu catálogo)
#
# ➡️ Vou falar rapidamente disso para já falarmos de Callback Protocols.
#
# Apesar de eu não gostar muito dos protocolos como classes abstratas, é
# importante que você saiba que dá para fazer eles se comportarem de maneira
# praticamente idêntica (com as ressalvas que já falei em aulas anteriores).
#
# Os benefícios que vejo nisso são:
# - Você não precisa escrever seu código às cegas (a tipagem vai te ajudar)
# - Você ganha qualquer implementação concreta do `Protocol`
# - Você pode definir métodos abstratos que geram erros no runtime
#
# Obs.: temos praticamente uma ABC aqui sem os benefícios da tipagem que falamos
# antes (isinstance, issubclass, etc...)
#
# Isso eu gravei em há 4 anos:
# Template method: https://youtu.be/-nSOKE4f2gA?si=Ds1TBFhcU0iYS0U0
#
# Doc Python
# https://typing.python.org/en/latest/spec/protocol.html#protocols
#
from abc import abstractmethod
from typing import Protocol, final

from utils import cyan_print, sep_print


class TemplateMethod[A, B](Protocol):
    @abstractmethod  # isso vai gerar erro em runtime
    def step_a(self) -> A: ...
    @abstractmethod
    def step_b(self) -> B: ...

    @final
    def run(self) -> tuple[A, B]:
        result_a = self.step_a()
        result_b = self.step_b()

        return result_a, result_b


class MakePair[T](TemplateMethod[T, T]):
    def __init__(self, a: T, b: T) -> None:
        self.a = a
        self.b = b

    def step_a(self) -> T:
        return self.a

    def step_b(self) -> T:
        return self.b


if __name__ == "__main__":
    sep_print()
    pair_maker = MakePair("Joãozinho", "Maria")
    pair = pair_maker.run()
    cyan_print(pair, f"{pair[0]} {pair[1]}")
    sep_print()

    pair_maker = MakePair[tuple[int, int]]((1, 2), (3, 4))
    pair_a, pair_b = pair_maker.run()
    cyan_print(pair_a, pair_b, sum(pair_a + pair_b))
    sep_print()
