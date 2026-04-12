from tkinter import Frame, Tk
from tkinter import ttk
from src.config import GAPI_BLOCK_SIZE, GAPI_COLORS, GAPI_WINDOW_BG, GAPI_WINDOW_TITLE
from src.engine import Engine


class Gapi(Engine):
    def __init__(self):
        super().__init__()
        self.__window = Tk()
        self.__window.title(GAPI_WINDOW_TITLE)
        self.__window.config(bg=GAPI_WINDOW_BG)

        self.__playground = ttk.Frame(self.__window)
        self.__playground.pack(expand=True, padx=10, pady=10)

        self.__rows, self.__cols = self.get_dimensions()
        self.__cells: list[list[Frame]] = []
        self.__create_widgets()

    def on_start(self) -> None:
        return

    def on_stop(self) -> None:
        self.__window.destroy()

    def view(self):
        for r in range(self.__rows):
            for c in range(self.__cols):
                bg_color = self.__get_color(r, c)
                if bg_color != self.__get_current_cell_color(r, c):
                    self.__cells[r][c].config(bg=bg_color)

        self.__window.update_idletasks()  # updates screen
        self.__window.update()

    def __get_current_cell_color(self, r: int, c: int) -> str:
        return str(self.__cells[r][c].cget("bg"))

    def __get_color(self, r: int, c: int) -> str:
        if self.is_alive(r, c):
            color = GAPI_COLORS["ALIVE"]
        else:
            if self.was_alive(r, c):
                color = GAPI_COLORS["WAS_ALIVE"]
            else:
                color = GAPI_COLORS["VOID"]
        return color

    def __create_widgets(self):
        for r in range(self.__rows):
            line: list[Frame] = []
            for c in range(self.__cols):
                frm = Frame(
                    self.__playground,
                    width=GAPI_BLOCK_SIZE,
                    height=GAPI_BLOCK_SIZE,
                    bg=GAPI_COLORS["VOID"],
                )
                frm.pack_propagate(False)
                frm.grid(row=r, column=c)
                line.append(frm)
            self.__cells.append(line)
