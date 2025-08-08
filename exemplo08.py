#
# Final do vídeo anterior sobre Classes...
#
# Neste vídeo vamos explorar vários recursos de tipagem moderna em Python:
# - dataclasses
# - classes abstratas (ABC)
# - métodos abstratos
# - padrão de projeto Singleton (com variação via cache)
# - @override, @final, ClassVar, Self
# - TypeAlias moderno com `type`
# - e um monte de lógica útil no meio do caminho.
#
# Etapas do código:
# - Criar a dataclass Person
# - Criar a classe Address e compor com a classe Person
# - Em Person, Address será um dict indexado, vamos usar TypeAlias com `type`
# - Criar um BaseAddress como ABC com pelo menos um @abstractmethod
# - Criar Address que herda de BaseAddress e implementa o método abstrato
# - Usar @override para garantir a assinatura correta
# - Criar CachedAddress com padrão Singleton por cache
# - Usar @final, ClassVar e Self para tipagem correta
# - ... veremos


from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar, Self, final, override

from utils import cyan_print, sep_print


class BaseAddress(ABC):
    def __init__(self, street: str, number: int) -> None:
        self.street: str = street
        self.number: int = number

    @abstractmethod
    def get_full_address(self) -> str: ...

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        attrs_list = [
            f"{k}={v!r}" for k, v in vars(self).items() if not k.startswith("_")
        ]
        attrs_str = ", ".join(attrs_list)
        return f"{cls_name}({attrs_str})"


class NewAddress(BaseAddress):
    @override
    def get_full_address(self) -> str:
        return f"{self.street} {self.number}"


class Address(BaseAddress):
    @override
    def get_full_address(self) -> str:
        return f"{self.street} {self.number}"


@final
class CachedAddress(Address):
    _cache: ClassVar[dict[str, Self]] = {}

    def __new__(cls, street: str, number: int) -> Self:
        fake_id = f"{street}{number}".lower().replace(" ", "")

        if fake_id in cls._cache:
            return cls._cache[fake_id]

        instance = super().__new__(cls)
        cls._cache[fake_id] = instance

        return instance

    def __init__(self, street: str, number: int) -> None:
        if not hasattr(self, "_initialized"):
            super().__init__(street, number)
            cyan_print(f"INICIALIZADO: {self}")
            self._initialized = True

    def clone(self) -> Self:
        return self


type Addresses = dict[int, Address]


@dataclass
class Person:
    name: str
    age: int
    _addresses: Addresses = field(
        default_factory=dict[int, Address],
        init=False,
        repr=False,
    )
    _new_address_index = 1

    def add_address(self, *addresses: Address) -> None:
        for address in addresses:
            self._addresses[self._new_address_index] = address
            self._new_address_index += 1  # 1, 2, 3, 4, etc...

    def get_address(self, index: int) -> Address | None:
        return self._addresses.get(index, None)


if __name__ == "__main__":
    sep_print()

    p1 = Person("Luiz", 18)
    a1 = Address("Address 1", 1)
    c1 = CachedAddress("Cached 1", 1)
    c2 = CachedAddress("Cached 2", 2)
    c21 = c2.clone()
    c3 = CachedAddress("Cached 3", 3)
    c31 = CachedAddress("Cached 3", 3)

    p1.add_address(a1, c1, c2, c3)

    cyan_print(p1)
    cyan_print(p1.get_address(1))
    cyan_print(p1.get_address(2))
    cyan_print(p1.get_address(3))

    sep_print()

    cyan_print(c2)
    cyan_print(c21)

    sep_print()
