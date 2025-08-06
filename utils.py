from collections.abc import Callable

from rich.console import Console

console = Console(markup=True, log_path=False, log_time=False)
rprint = console.log


# Olha aí o seu Callable super genéric.
# O '...' representa qualquer coisa
def make_print(style: str) -> Callable[..., None]:
    # closure, lembra?
    def fake_print(*values: object) -> None:
        return console.log(*values, style=style)

    return fake_print


def sep_print() -> None:
    rprint(f"\n{80 * '―'}\n", style="yellow")


red_print = make_print(style="red")
green_print = make_print(style="green")
yellow_print = make_print(style="yellow")
blue_print = make_print(style="blue")
magenta_print = make_print(style="magenta")
cyan_print = make_print(style="cyan")
