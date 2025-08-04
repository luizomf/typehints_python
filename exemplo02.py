#
# Como usar os Type Checkers?
#
# Type Checkers geralmente são programas de linha de comando.
# No nosso ambiente (usando a ferramenta `uv`), podemos instalar o Pyright com:
#   uv tool install pyright
# Também podemos rodar diretamente, sem instalar globalmente:
#   uvx pyright ...
#
# Mas essa não é a forma mais prática. A forma mais prática é configurar o
# Type Checker no seu editor (VS Code, Neovim, PyCharm, etc).
# Assim, ele vai te alertar em tempo real sempre que houver algum problema.
# (No nosso "Ambiente Python 2025", isso já vem pronto).
#
# Agora vamos ver um exemplo de tipagem simples.
# A maioria desses tipos nem precisa ser anotada, o Python (e o editor) já sabe.
# Mas ao anotar, você ganha mais controle e impede alterações de tipo futuras.
#

# Tipos básicos (explícito e implícito)

# Python 3.13.5

from typing import Final

nome: str = "Luiz Otávio"
x: int = 22
y: float = 23.33
c: complex = 3 + 4j
is_valid: bool = True
data: bytes = b"whatever"


# Constantes
# Essa constante não costuma ser reatribuída, então a tipagem é redundante.
# O próprio valor já deixa claro que é uma string.
CONSTANTE = "valor constante"


# Coleções
lista_numeros: list[int] = [1, 2, 3]
tupla_dois_valores: tuple[str, int] = ("Valor", 234)
tupla_varios: tuple[str, ...] = "a", "b", "c", "..."
conjunto: set[int] = {1, 2, 3, 4}
conjunto_imutavel: frozenset[int] = frozenset([2, 3, 4, 5])
dicionario: dict[str, str] = {"chave": "valor", "chave2": "valor2"}
numeros: range = range(10)

# Outros tipos
nada: None = None  # Representa ausência de valor
qualquer_coisa: object = 123  # Pode ser qualquer objeto
tipo: type[str] = str  # Referência ao tipo 'str' em si (não uma string)

# Constantes novamente
CONSTANTE_DOIS: Final[list[str]] = ["a", "b"]
constante_tres: Final[dict[str, int]] = {"numero": 123, "outro_numero": 432}
