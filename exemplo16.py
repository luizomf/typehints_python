#
# O princípio da substituição de Liskov
#
# MediaPlayer -> Super classe
# Atributos:
# - Privados: current_volume, max_volume, min_volume
# - Propriedades de leitura: volume,max_volume, min_volume
# Métodos:
# - increase_volume: aumentar volume até o máximo.
# - decrease_volume: diminuir volume até o mínimo.
#


from typing import Final, override


class MediaPlayer:
    def __init__(self) -> None:
        self._current_volume: int = 0  # Private, não toque
        self._max_volume: Final[int] = 100  # Está claro que isso é "invariante".

    @property  # read
    def volume(self) -> int:
        return self._current_volume

    @property  # read
    def max_volume(self) -> int:
        return self._max_volume

    def increase_volume(self) -> None:
        if self._current_volume < self._max_volume:
            self._current_volume += 1
            print("Increased:", self._current_volume)


class FancyMediaPlayer(MediaPlayer):
    def __init__(self) -> None:
        super().__init__()
        self._eardrums_protection = 10

    @override
    def increase_volume(self) -> None:
        # Isso era pra ser invariante: só essa intenção já quebrou a regra
        # Mas o type checker não confere a sua lógica
        max_volume = self._max_volume - self._eardrums_protection

        if self._current_volume < max_volume:  # Pré-condição mais restritiva
            self._current_volume += 1

        # Olha eu quebrando uma pós-condição escondida aqui
        # O filho vai entregar um volume "mais fraco" que o pai".
        # O pai promete 100, mas o filho entrega 90.
        # Isso seria uma pós-condição implícita


def max_volume_btn_action(mp: MediaPlayer) -> None:
    for _ in range(mp.max_volume):
        mp.increase_volume()

    assert mp.volume == mp.max_volume, "What went wrong here?"


if __name__ == "__main__":
    fancy = FancyMediaPlayer()
    max_volume_btn_action(fancy)
