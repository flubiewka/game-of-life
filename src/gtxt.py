from src.engine import Engine

ANSI = {
    # color reset
    "RESET": "\033[0m",
    # background
    # "B_BLACK": "\033[40m",
    "B_RED": "\033[41m",
    "B_GREEN": "\033[42m",
    "B_DARK_GREEN": "\033[48;5;34m",
    # "B_YELLOW": "\033[43m",
    # "B_BLUE": "\033[44m",
    # "B_WHITE": "\033[47m",
    # cls
    "CLEAR_SCREEN": "\033[H\033[J",
    "CURSOR_HOME": "\033[H",
    # cursor
    "HIDE_CURSOR": "\033[?25l",
    "SHOW_CURSOR": "\033[?25h",
    # alt screen for clean ending
    "ENTER_ALT_SCREEN": "\033[?1049h",
    "EXIT_ALT_SCREEN": "\033[?1049l",
}


class Gtxt(Engine):
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
