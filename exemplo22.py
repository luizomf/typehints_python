#
# O problema da duração do vídeo (REAL)
#
# ⚠️ ATENÇÃO: tecnicamente eu não precisaria de nada disso que vou mostrar a seguir,
# meu problema estava entre str e float apenas. Mas estou replicando o exemplo
# com objetos para termos mais exemplos de tipagem.
#
# Estive montando um script para concatenar vários vídeos de uma playlist e um
# único vídeo enorme.
#
# -> aula1.mp4 (120 segundos) aula2.mp4 (60 segundos) aula3.mp4 (120 segundos)
# -> aulão.mp4 (300 segundos)
#
# Os problemas que encontrei é que eu precisava converter a duração do vídeo de
# segundos para horas e de horas para segundos para criar os capítulos do YouTube.
# Em resumo, precisava somar os segundos para pegar o timestamp correto de onde
# uma aula terminava e outra começada, depois converter os segundos em horas
# para gerar "HH:MM:SS - Título do capítulo" para o YouTube.
#
# -> aula1.mp4 (00:02:00) aula2.mp4 (00:01:00) aula3.mp4 (00:02:00)
# -> aulão.mp4 (00:05:00)


# O exemplo abaixo é só uma forma que encontrei de representar o problema para
# solucionarmos a tipagem juntos.


from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from utils import cyan_print, sep_print

type StrIntFloat = str | int | float


class Duration[T: StrIntFloat]:
    def __init__(self, value: T) -> None:
        self._value: T = value

    @property
    def value(self) -> T:
        return self._value

    def __repr__(self) -> str:
        return f"Duration({self._value!r})"


@dataclass
class VideoInfo[T: StrIntFloat]:
    name: str
    duration_seconds: Duration[T]

    @property
    def duration_time(self) -> str:  # precisamos corrigir
        if isinstance(self.duration_seconds.value, int | float):
            return seconds_to_time(self.duration_seconds.value)
        return self.duration_seconds.value


def seconds_to_time(seconds: float) -> str:
    delta = datetime(1, 1, 1, 0, 0, 0, tzinfo=UTC) + timedelta(seconds=seconds)
    return f"{delta:%H:%M:%S}"


if __name__ == "__main__":
    sep_print()

    d1 = Duration(60)  # ⚠️
    d2 = Duration("00:10:00")

    v1 = VideoInfo("aula1.mp4", d1)  # ⚠️
    v2 = VideoInfo("aula2.mp4", d2)

    cyan_print(v1, v1.duration_time)  # ⚠️
    cyan_print(v2, v2.duration_time)
    cyan_print(v2, v2.duration_seconds)

    sep_print()
