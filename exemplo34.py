################################################################################
#
# TypedDict - Discriminated Union
#
# Já pensou em decidir um tipo com base em determinado valor? Podemos fazer isso
# e com Discriminated Union (muito comum no Typescript, menos comum em Python).
# Nesse tipo de tipagem, geramos uma tag em uma determinada chave e decidimos
# a estrutura da tipagem com base nessa tag.
#
# Por exemplo, pensa em uma `Response` do servidor. Ela pode ter variações.
# Se o `status` for `ok`, então a Response pode trazer a chave `data`.
# Mas se o `status` for `error`, então a Response pode trazer a chave `message`.
#
# Vídeo sobre Match/Case:
# https://youtu.be/2f_5LRQV3k0?si=8Lt2T_9Cq0EPcCc7
#
################################################################################

from typing import Literal, TypedDict

from utils import cyan_print, green_print, red_print, sep_print


class ResponseSuccess(TypedDict):
    status: Literal["ok"]  # tag
    data: str  # exemplo para não termos que modelar dados aqui


class ResponseError(TypedDict):
    status: Literal["error"]  # tag
    message: str  # exemplo novamente


type Response = ResponseSuccess | ResponseError  # Discriminated Union com tag status


def handle_response(res: Response) -> None:
    match res["status"]:
        case "ok":
            # Se status é ok, o tipo só pode conter agora "data" (não "error")
            # reveal_type(res)  # O tipo de res é ResponseSuccess
            green_print("RESPONSE OK ✅", res["data"])
            return
        case "error":
            # Se status é error, o tipo só pode conter agora "message" (não "data")
            # reveal_type(res)  # O tipo de res é ResponseError
            red_print("ERROR ❌", res["message"])
            return

    # Por conta da análise do Pyright e nossa tipagem,
    # na teoria, esse código não deveria ser alcançado.
    # Mas eu vou forçar um erro depois
    red_print("💥 I can't handle this response")


if __name__ == "__main__":
    sep_print()

    response_success: ResponseSuccess = {"status": "ok", "data": "Here is your result"}
    handle_response(response_success)
    cyan_print()
    sep_print()

    response_error: ResponseError = {"status": "error", "message": "BadRequest"}
    handle_response(response_error)
    cyan_print()
    sep_print()

    wrong_response = {"status": "any"}
    handle_response(wrong_response)
    cyan_print()
    sep_print()

################################################################################
