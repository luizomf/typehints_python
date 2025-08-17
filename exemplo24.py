#
# Vários princípios da programação num código simples
#
# Nesse código, quero te mostrar como aplicar TODOS os princípios do SOLID de
# uma vez só. De forma simples você vai entender todos ele sem usar tipagem e
# subtipagem nominal.
#
from typing import Protocol

from utils import sep_print


class SupportsRead(Protocol):
    path: str

    def read(self) -> object: ...


class JsonManager:
    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> dict[str, object]: ...  # isso será covariância


class CsvManager:
    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> str: ...  # será covariância de novo


def load_data(reader: SupportsRead) -> object:
    # reader como JsonManager ou CsvManager, seria depender de algo concreto
    # usando protocol estamos dependendo de uma abstração:
    # Isso é chamado de: Dependency inversion principle
    # Além disso, o protocolo SupportsRead só tem o método que ele precisa ter
    # Este outro princípio é chamado de: Interface Segregation Principle
    # Aqui também temos substituição: lembra do Liskov Substitution principle?
    # Por falar nisso, talvez eu nem precise mais tocar no código dessa função:
    # portanto, Open Closed Principle.
    # Mais um pra você: essa função só tem um único motivo para mudar, SupportsRead.
    # Chamamos esse de Single Responsibility Principle:
    # E juntos, com pouquíssimas linhas de código, implementamos todo o SOLID.
    return reader.read()


if __name__ == "__main__":
    sep_print()

    json_data = load_data(JsonManager("file.json"))
    csv_data = load_data(CsvManager("file.csv"))

    sep_print()
