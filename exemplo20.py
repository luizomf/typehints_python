#
# TypeVar e funções genéricas no Python moderno - Aula 8
#
# Usaremos a nova sintaxe definida pela PEP 695 (Python >=3.12)
# https://docs.python.org/3/whatsnew/3.12.html#pep-695-type-parameter-syntax
#

################################################################################

# O argumentos um pra um: cada argumento tem o seu tipo


def multiple_args[A, B, C](a: A, b: B, c: C) -> A | B | C: ...


ma = multiple_args(1, "dois", [3])  # int | str | list[int]
reveal_type(ma)

################################################################################


# Várias ocorrências do mesmo tipo com upper bound
def add_number[T: float](a: T, b: T) -> T: ...


an = add_number(1, True)  # (bool <: int <: float)
# Aqui o Pyright adotou um comportamento literal mesmo. Já o mypy cravou na doc.
# Doc: Using a bounded type variable means that the TypeVar will be solved
# using the most specific type possible
# reveal_type(an)  # int | bool (de acordo com Pyright)
# mypy -> builtins.int


################################################################################


# Várias ocorrências do mesmo tipo com constraint
def only_one_type_please[T: (str, bytes)](a: T, b: T) -> T: ...


# an = only_one_type_please("Abc", b"Abc")  # str (a restrição só permite UM dos tipos)
anb = only_one_type_please(b"Abc", b"Abc")  # bytes
ans = only_one_type_please("Abc", "Abc")  # str


################################################################################


# Valor padrão para o tipo
def default[T = str | int](a: T | None = None, b: T | None = None) -> T: ...


anb = default()  # str | int # Não teria como inferir aqui


################################################################################
