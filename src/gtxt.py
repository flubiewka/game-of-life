from src.config import ANSI
from src.engine import Engine


class Gtxt(Engine):
    def on_start(self) -> None:
        print(ANSI["ENTER_ALT_SCREEN"] + ANSI["HIDE_CURSOR"], end="", flush=True)

    def on_stop(self) -> None:
        print(ANSI["SHOW_CURSOR"] + ANSI["EXIT_ALT_SCREEN"], end="", flush=True)

    def view(self) -> None:
        print(ANSI["CURSOR_HOME"], end="")

        rows, cols = self.get_dimensions()
        full_field: list[str] = []

        for r in range(rows):
            line: list[str] = []
            for c in range(cols):
                if self.is_alive(r, c):
                    color = ANSI["B_RED"]
                else:
                    if self.was_alive(r, c):
                        color = ANSI["B_DARK_GREEN"]
                    else:
                        color = ANSI["B_GREEN"]
                line.append(f"{color}  ")
            full_field.append("".join(line) + ANSI["RESET"])

        print("\n".join(full_field), flush=True)
