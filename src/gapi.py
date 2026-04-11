from tkinter import Frame, Tk
from tkinter import ttk
from src.engine import Engine

COLORS = {"VOID": "#13a10e", "WAS_ALIVE": "#00af00", "ALIVE": "#c50f1f"}
BLOCK_SIZE = 20


class Gapi(Engine):
    def __init__(self):
        super().__init__()
        self.__window = Tk()
        self.__window.title("Game Of Life")
        self.__window.config(bg="#333333")

        self.__playground = ttk.Frame(self.__window)
        self.__playground.pack(expand=True, padx=10, pady=10)

        self.__rows, self.__cols = self.get_dimensions()
        self.__cells: list[list[Frame]] = []
        self.__createWidgets()

    def view(self):
        for r in range(self.__rows):
            for c in range(self.__cols):
                self.__cells[r][c].config(bg=self.__getColor(r, c))

        self.__window.update_idletasks()  # updates screen
        self.__window.update()

    def __getColor(self, r: int, c: int) -> str:
        if self.is_alive(r, c):
            color = COLORS["ALIVE"]
        else:
            if self.was_alive(r, c):
                color = COLORS["WAS_ALIVE"]
            else:
                color = COLORS["VOID"]
        return color

    def __createWidgets(self):
        for r in range(self.__rows):
            line: list[Frame] = []
            for c in range(self.__cols):
                frm = Frame(
                    self.__playground,
                    width=BLOCK_SIZE,
                    height=BLOCK_SIZE,
                    bg=self.__getColor(r, c),
                )
                frm.pack_propagate(False)
                frm.grid(row=r, column=c)
                line.append(frm)
            self.__cells.append(line)
