#
# Sequence - Implementando e usando Sequence
#
# https://docs.python.org/3/reference/datamodel.html#emulating-container-types
#
# Use `Sequence[T]` sempre que você precisar de uma coleção ordenada, assim como
# `list[T]` ou `tuple[T]`. Porém `Sequence[T]` não expõe operações de inserção,
# alteração ou remoção. Basicamente, temos uma coleção ordenada imutável.
# Ela suporta toda a parte de leitura: `len(obj)`, `obj[i]`, `obj[a:b:c]`, etc.
# O foco maior dessa aula será em implementar o protocolo.
# Ao implementar `Sequence[T]`, temos que definir: `__getitem__` e `__len__`.
#
from collections.abc import Iterator, Sequence
from typing import overload, override

from utils import cyan_print, sep_print

type T = str


class ReadOnlySequence(Sequence[T]):
    def __init__(self, *args: T) -> None:
        self._data: dict[int, T] = {}
        self._index = 0
        self._next_index = 0

        self._add_initial_value(*args)

    def _add_initial_value(self, *args: T) -> None:
        for arg in args:
            self._data[self._index] = arg
            self._index += 1

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    @override
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, int):
            return self._data[index]

        values = list(self._data.values())[index]
        return ReadOnlySequence(*values)

    @override
    def __len__(self) -> int:
        return self._index

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        if not self._data or self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1

        return value

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        attrs = ", ".join([f"{v!r}" for v in self._data.values()])
        return f"{cls_name}({attrs})"


if __name__ == "__main__":
    s1 = ReadOnlySequence("a", "b", "c")
    sep_print()

    cyan_print(s1)
    cyan_print(s1[0])
    cyan_print(s1[1])
    cyan_print(s1[0:2])
    cyan_print(list(reversed(s1)))
    cyan_print(len(s1))

    iterator = iter(s1)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

    print("for")
    for value in s1:
        print(value)

    print("for")
    for value in s1:
        print(value)

    sep_print()
