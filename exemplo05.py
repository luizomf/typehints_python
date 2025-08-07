#
# Classes - Vamos relembrar (Vai ser muito importante)
#
# RUNTIME (Código em tempo de execução):
# Classes são fábricas de objetos. Elas funcionam como moldes para gerar novas
# estruturas de dados na linguagem.
# Por exemplo: ao criar a classe `Animal`, o que você fez foi criar uma nova
# fábrica de objetos do tipo `Animal`.
# Tudo o que foi definido em `Animal` (o molde), será passado para os objetos
# fabricados pela classe `Animal`.
# Esses objetos agora são chamados e "instâncias" da classe `Animal`.
# Um `Dog` criado por `Animal` é uma instância de `Animal`. Assim como um `Cat`.
# Dentro da classe, podemos nos referir à instância que está sendo criada
# usando a palavra `self`.
# Classe == Molde (a fábrica) | Instância == O que foi fabricado pela classe

from utils import cyan_print, sep_print


class Animal:
    def __init__(self, name: str):
        self.name: str = name

    def make_sound(self) -> None:
        raise NotImplementedError


if __name__ == "__main__":
    dog = Animal("Dog")
    cat = Animal("Cat")

    sep_print()

    cyan_print(f"{dog.name = !r}")
    cyan_print(f"{cat.name = !r}")

    sep_print()
