#
# Protocol e Structural Subtyping: tipagem estática no Python
#
# Até agora vimos o Python trabalhando com tipagem nominal, ou seja,
# uma classe só é subtipo de outra se você declarar isso explicitamente.
# Exemplo: se `B` herda de `A`, então `B` é um `A`. Isso é subtipagem nominal.
#
# Só que no dia a dia o Python é famoso pelo "duck typing":
# "se anda como um pato e faz quack como um pato, eu trato como um pato".
# Ou seja, no runtime o Python não tá checando herança, mas sim se
# determinado método ou atributo existe no objeto.
#
# A boa notícia: na tipagem estática também temos um equivalente a esse
# duck typing, e isso se chama Tipagem estrutural (Structural Typing).
#
# Para trabalhar com tipagem estrutural no Python moderno, usamos `Protocol`.
# Ele permite que a gente defina um "contrato" de métodos/atributos que
# qualquer classe pode cumprir, mesmo sem declarar herança.
#
# Repara que "contrato" aparece de novo: antes, com ABC, o contrato é nominal e
# tem efeito em runtime (subclasse sem método abstrato não instancia).

# Com Protocol, o contrato é estrutural e funciona principalmente no estático, o
# type checker aceita qualquer objeto com a "forma" certa. Em runtime, o
# protocolo é uma classe especial, mas não valida implementações por conta própria.
#
# Obs.: se você já programou em Typescript, vai se sentir em casa, os
# Protocols funcionam de forma bem parecida com as interfaces lá.
#
# https://typing.python.org/en/latest/reference/protocols.html#predefined-protocol-reference
#
from dataclasses import dataclass
from typing import Protocol

from utils import cyan_print, sep_print


class SupportsTalk(Protocol):
    name: str

    def talk(self, phrase: str) -> None: ...


@dataclass
class Person:
    name: str

    def talk(self, phrase: str) -> None:
        cyan_print(phrase)


@dataclass
class Toy:
    name: str

    def talk(self, phrase: str) -> None:
        cyan_print(phrase)


def talk(obj: SupportsTalk, phrase: str) -> None:
    cyan_print(f"{obj.__class__.__name__}({obj.name}) will talk")
    obj.talk(phrase)


if __name__ == "__main__":
    sep_print()

    person1 = Person("Luiz")
    toy1 = Toy("Samsung")
    # supports_talk = SupportsTalk()  # cannot instantiate Protocol class...

    talk(person1, "I know how to talk.")
    talk(toy1, "I know how to talk.")

    sep_print()
