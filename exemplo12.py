#
# Invariância em genéricos padrão
#
# Doc: https://docs.python.org/3/library/collections.abc.html
#
# invariant: os tipos precisam ser idênticos; não existe variância de subtipagem aqui.
# Regra prática: quando o tipo aparece em posições de ENTRADA e SAÍDA (mutáveis),
# o checker não pode nem co- nem contravariar com segurança, sobre apenas invariância.
#
# Exemplos clássicos (mutáveis): list[T], set[T], dict[K, V], deque[T],
# MutableSequence[T], MutableSet[T], MutableMapping[K, V].

#
# Aqui vai um exemplo clássico, eu quero uma lista de strings ou inteiros
# Podemos imaginar que list[`str | int`] aceitaria:
# - Uma lista de strings
# - Uma lista de inteiros
# - Uma lista de strings e inteiros
# Mas não, SÓ UMA LISTA DE STRING E INTEIROS (Invariância)
def handle_str_int(items: list[str | int]) -> None: ...


my_list: list[str] = ["a", "b"]
handle_str_int(my_list)  # type checker error

# Isso também faz sentido demais. Se a lista acima é mutável, a função poderia
# adicionar um inteiro nela e acabar mudando o tipo da minha lista sem que eu
# percebesse. No final, `my_list` se tornaria `list[str | int]` e quebraria
# outras partes do programa.
