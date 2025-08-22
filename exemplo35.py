from typing import NewType

from utils import cyan_print, sep_print

################################################################################
#
# NewType - Iguais, mas diferentes 🤯
#
# Com NewType, você pode criar um novo tipo para o Type Checker com base em
# outro tipo. O Type Checker deve considerar seu novo tipo como se ele fosse
# uma subclasse do tipo base. No runtime, o tipo original DO VALOR será usado,
# mas para o Type Checker seu novo tipo "É UM" tipo base.
#
# Isso ajuda a prevenir erros lógicos no seu programa, porque ao invés de esperar
# um `int` aleatório, você pode passar a esperar por um tipo específico em
# locais onde isso importa.
#
# Vejamos um exemplo mais real para você entender melhor o problema e a solução:
#
# No meu e-commerce, tenho duas funções que obtém IDs de `posts` e `users`.
# Vamos considerar esses IDs como `int` para manter a consistência com o que eu
# disse antes.
#
# Problema: se em algum momento eu passar o ID do user para a função de
# `get_post`, ou vice versa, o Type Checker deve aceitar, já que ambos os IDs
# de `posts` e `users` são `int`.
#
# Uma possível solução para isso seria criar uma classe à parte para cada ID.
# Isso geraria um novo tipo, mas com impacto de objeto em desempenho (tem overhead).

# Solução: USAR `NewType`! Com ele geramos um novo tipo para o Type Cheker,
# mas só no campo do tipo. Isso tem quase zero impacto em desempenho e para a
# checagem de tipos, funciona como o tipo distinto.
#
# Vamos replicar meu exemplo em um código concreto já usando `NewType`.
#
################################################################################

# Ambos NewTypes abaixo são `int` normais em runtime
# Para o Type Checker, serão dois tipos distintos
UserId = NewType("UserId", int)  # Para o Type Checker: `UserId` <: `int`
PostId = NewType("PostId", int)  # Para o Type Checker: `PostId` <: `int`


################################################################################


# Antes essa função esperaria um `int`, agora ela só aceita `UserId`.
def get_user(user_id: UserId) -> int:
    return user_id


# Mesma coisa aqui, agora só aceitamos `PostId`.
def get_post(post_id: PostId) -> int:
    return post_id


################################################################################


if __name__ == "__main__":
    sep_print()

    user_id = UserId(42)  # IMPORTANTE: Atenção ao valor (vamos voltar nisso adiante)
    post_id = PostId(2)

    user1 = get_user(user_id)  # ✅ Type Checker aceita perfeitamente
    post1 = get_post(post_id)  # ✅

    # user2 = get_user(post_id)  # ❌ Type Checker Rejeita
    # post2 = get_post(user_id)  # ❌

    cyan_print(f"{user1=}", type(user1))  # Runtime: 42 int
    cyan_print(f"{post1=}", type(post1))  # Runtime: 2 int

    # Cuidado: result_is_int é obviamente do tipo `int`
    result_is_int = user_id * post_id  # O Type Checker não liga com isso
    cyan_print(f"{result_is_int=}", type(result_is_int))  # <class 'int'>

    sep_print()

################################################################################
