from datetime import UTC, datetime, tzinfo
from typing import Protocol, overload

from utils import cyan_print, sep_print

################################################################################
#
# Callback Protocol com overloads complexos
#
# Montei esse exemplo para mostrar o poder que você tem em mãos ao utilizar
# um callback protocol. Você conseguirá tipar QUALQUER coisa que souber a
# assinatura.
# É um exemplo um pouco mais complexo talvez até "inútil". Eu forcei o uso
# de Callback Protocol para mostrar exemplos. Conseguiríamos o mesmo resultado
# talvez com funções BEM MAIS simples.
# Porém, esse exemplo vai te dar MUITO IDEIAS... 🤯🤯🤯
#
################################################################################
#
# Qual problema queremos resolver?
#
# Suponha que eu queira criar um wrapper que envolve o datetime do Python para
# flexibilizar a criação de datas com base no tipo dos argumentos enviados para
# esse meu wrapper.
#
# As regras são:
# - Se eu enviar uma string, o wrapper deve entender que é para usar o método
#   `strptime` para criar uma nova data com base na string (também no formato).
# - Se eu enviar um inteiro ou float, meu wrapper precisa chamar `fromtimestamp`.
#   e criar uma data com base no timestamp.
# - Se eu enviar uma tupla com inteiros, meu wrapper precisa criar uma data
#   usando ano, mês, dia, e assim por diante.
#
# Para solucionar isso, podemos usar um padrão chamado de `Dispacher`, ou seja,
# ele recebe os argumentos e despacha para o local adequado.
#
# Porém, o nosso dispatcher só vai escolher o método. Vamos criar outra função
# que vai usar o dispatcher para executar tudo isso (a cola final para tudo).
#
# Obs.: como eu já disse, isso pode ser desnecessário, mas eu quero te mostrar
# como ficaria toda a tipagem completa nesse cenário mais complexo.
#
################################################################################

# Eu só criei esses protocolos para "replicar" os métodos `strptime` e
# `fromtimestap` de `datetime`. Apenas como exercício para que você veja
# o que é possível fazer com Callback Protocols.

type Date3 = tuple[int, int, int]
type Date4 = tuple[int, int, int, int]
type Date5 = tuple[int, int, int, int, int]
type Date6 = tuple[int, int, int, int, int, int]
type Date7 = tuple[int, int, int, int, int, int, int]
type DateParts = Date3 | Date4 | Date5 | Date6 | Date7


class Strptime(Protocol):
    def __call__(self, date_string: str, format: str, /) -> datetime: ...


class FromTimestamp(Protocol):
    def __call__(self, timestamp: float, *, tz: tzinfo = ...) -> datetime: ...


# O Callback Protocol abaixo eu crie para te mostrar exemplos de overload muito
# complicados. Esses overloads decidem o que retornar baseado no que estou
# recebendo.


class DatetimeDispatcher(Protocol):
    @overload
    def __call__(
        self,
        value: str,
        in_format: str,
    ) -> Strptime: ...
    @overload
    def __call__(
        self,
        value: DateParts,
    ) -> type[datetime]: ...
    @overload
    def __call__(
        self,
        value: float,
    ) -> FromTimestamp: ...


################################################################################

# O trabalho dessa função é decidir qual método de "datetime" é o mais adequado
# baseado nos tipos que ela recebeu.


@overload
def datetime_dispacher(
    value: str,
    in_format: str,
) -> Strptime: ...
@overload
def datetime_dispacher(
    value: DateParts,
) -> type[datetime]: ...
@overload
def datetime_dispacher(
    value: float,
) -> FromTimestamp: ...
def datetime_dispacher(
    value: str | DateParts | float,
    in_format: str | None = None,
) -> Strptime | FromTimestamp | type[datetime]:
    if isinstance(value, str):
        if not in_format:
            msg = f"You must inform the date format for {value!r}"
            raise ValueError(msg)

        return datetime.strptime

    if isinstance(value, tuple):
        return datetime

    return datetime.fromtimestamp


################################################################################

# A função que usa isso tudo tem a tarefa de criar e executar o dispatcher
# passando o valores corretos para dentro dele sem quebrar a tipagem.
# Como cada chamada é um pouco diferente da outra, temos que garantir os tipos
# para cada uma delas.


@overload
def create_date(
    value: str,
    dispatch: DatetimeDispatcher,
    *,
    in_format: str,
) -> datetime: ...
@overload
def create_date(
    value: DateParts,
    dispatch: DatetimeDispatcher,
) -> datetime: ...
@overload
def create_date(
    value: float,
    dispatch: DatetimeDispatcher,
) -> datetime: ...
def create_date(
    value: str | DateParts | float,
    dispatch: DatetimeDispatcher,
    in_format: str | None = None,
) -> datetime:
    if isinstance(value, str):
        if not in_format:
            msg = f"You must inform the date format for {value!r}"
            raise ValueError(msg)
        return dispatch(value, in_format=in_format)(value, in_format)
    if isinstance(value, tuple):
        dt_field_keys = [
            "year",
            "month",
            "day",
            "hour",
            "minute",
            "second",
            "microsecond",
        ]
        dt_kwargs = dict(zip(dt_field_keys, value, strict=False))
        return dispatch(value)(**dt_kwargs, tzinfo=UTC)

    # int or float
    return dispatch(value)(value)


################################################################################

# Bora testar tudo


if __name__ == "__main__":
    sep_print()

    # o mesmo que datetime
    date1 = create_date((1, 1, 1, 10, 25, 59), datetime_dispacher)
    # o mesmo que datetime.strptime
    date2 = create_date("2025-08-19", datetime_dispacher, in_format="%Y-%m-%d")
    # o mesmo que datetime.fromtimestamp
    date3 = create_date(1755696515, datetime_dispacher)

    datefmt = "%d/%m/%Y"
    timefmt = "%H:%M:%S"
    cyan_print(f"{date1:{timefmt}}")
    cyan_print(f"{date2:{datefmt}}")
    cyan_print(f"{date3:{datefmt}}")


################################################################################
