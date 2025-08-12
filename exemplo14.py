#
# Liskov Substitution Principle ou Princípio da substituição de Liskov
#
# Artigo: https://www.otaviomiranda.com.br/2025/liskov-substitution-principle-lsp-solid/
#
# Pré-condições: O subtipo não pode ser mais restritivo que o tipo base.
# Contravariância = C[A] <: C[B]
# Pós-condições: O subtipo não pode enfraquecer as condições do tipo base.
# Covariância = C[B] <: C[A]
# Invariantes: O subtipo deve manter todos os invariantes do tipo base.
# Invariância = C[A] != C[B]
#
from collections.abc import Collection, MutableSequence, Sequence
from typing import override


class Base:
    def execute(self, param: Sequence[int]) -> Sequence[int]: ...


class SubType(Base):
    @override
    def execute(self, param: Collection[int]) -> MutableSequence[int]: ...
