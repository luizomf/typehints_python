#
# Type Hints em Funções e "Callables"
#
# Na aula anterior, vimos como dar tipos explíticos e implícitos para as
# variáveis e coleções. Agora ver funções (callables).
#
# Preciso tipar Funções?
# Quando criamos uma função, também precisamos criar um "manual de instruções"
# do seu uso. Nesse cenário, documentação ajuda bastante, mas a tipagem é o que
# vai garantir que ninguém chame a função com valores incorretos.
#
# O que precisamos tipar?
# - PARÂMETROS: Diferente de uma variável como `x = 10`, um parâmetro
#     de função não tem um valor inicial para o Type Checker "adivinhar"
#     o seu tipo. Por isso, é ESSENCIAL que nós informemos o tipo de cada
#     argumento que a função espera receber.
# - RETORNO: Também devemos sempre tipar o valor que a função devolve
#     usando a sintaxe da seta `->`. Se uma função não retorna nada
#     (apenas executa uma ação, como um `print`), o tipo de retorno
#     correto é `None`. Isso evita que a gente tente usar o resultado de
#     uma função que, na verdade, não retorna nada.
#
# Vamos ver um exemplo simples de tipagem para começar:

from utils import cyan_print, sep_print

sep_print()


def remove_duplicates(items: list[str]) -> list[str]:
    # `dict.fromkeys` gera um dicionário a partir da lista.
    to_dict = dict.fromkeys(items)
    # `list` converte o dict em lista, remove as duplicatas e mantém a ordem.
    return list(to_dict)


# Será removido ❌:                       ❌        ❌        ❌
list_with_duplicates = ["luiz", "a", "b", "a", "c", "a", "d", "luiz"]
unique_items = remove_duplicates(list_with_duplicates)
# Saída - ['luiz', 'a', 'b', 'c', 'd']
cyan_print(f"{unique_items = }")
sep_print()


def is_image_file(filename: str) -> bool:
    # Algumas extensões comuns de imagens
    extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    # Garante que o nome do arquivo está em letras minúsculas sempre
    name_lowercase = filename.lower()
    # Termina com alguma das extensions ou não?
    return name_lowercase.endswith(extensions)


# Uso
filename = "arquivo.exe"
cyan_print(f" {is_image_file(filename) = } | {filename = }")
filename = "imagem.JPEG"
cyan_print(f" {is_image_file(filename) = } | {filename = }")
filename = "foto.png"
cyan_print(f" {is_image_file(filename) = } | {filename = }")
filename = "meme.gif"
cyan_print(f" {is_image_file(filename) = } | {filename = }")
sep_print()
