from src.config import ANSI
from src.engine import Engine


class Gtxt:
    def __init__(self, engine: Engine):
        self.__engine = engine

    def on_start(self) -> None:
        # Switch to alternate screen buffer for clean animation.
        print(ANSI["ENTER_ALT_SCREEN"] + ANSI["HIDE_CURSOR"], end="", flush=True)

    def on_stop(self) -> None:
        print(ANSI["SHOW_CURSOR"] + ANSI["EXIT_ALT_SCREEN"], end="", flush=True)

    def view(self) -> None:
        # Redraw from top-left without clearing terminal history.
        print(ANSI["CURSOR_HOME"], end="")

        rows, cols = self.__engine.get_dimensions()
        full_field: list[str] = []

        for r in range(rows):
            line: list[str] = []
            for c in range(cols):
                if self.__engine.is_alive(r, c):
                    color = ANSI["B_RED"]
                else:
                    if self.__engine.was_alive(r, c):
                        color = ANSI["B_DARK_GREEN"]
                    else:
                        color = ANSI["B_GREEN"]
                line.append(f"{color}  ")
            # Reset color at line end to keep terminal state sane.
            full_field.append("".join(line) + ANSI["RESET"])

        print("\n".join(full_field), flush=True)
