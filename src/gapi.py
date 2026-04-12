from tkinter import Canvas, TclError, Tk
from src.config import GAPI_BLOCK_SIZE, GAPI_COLORS, GAPI_WINDOW_BG, GAPI_WINDOW_TITLE
from src.engine import Engine


class Gapi(Engine):
    def __init__(self):
        super().__init__()
        # Tk window is created once and reused every frame.
        self.__window = Tk()
        self.__window.title(GAPI_WINDOW_TITLE)
        self.__window.config(bg=GAPI_WINDOW_BG)

        self.__rows, self.__cols = self.get_dimensions()
        canvas_width = self.__cols * GAPI_BLOCK_SIZE
        canvas_height = self.__rows * GAPI_BLOCK_SIZE
        self.__canvas = Canvas(
            self.__window,
            width=canvas_width,
            height=canvas_height,
            bg=GAPI_WINDOW_BG,
            highlightthickness=0,
        )
        self.__canvas.pack(expand=True, padx=10, pady=10)

        self.__cells: list[list[int]] = []
        # Keep last painted color to avoid unnecessary canvas updates.
        self.__cell_colors_cache: list[list[str]] = []
        self.__create_widgets()

    def on_start(self) -> None:
        return

    def on_stop(self) -> None:
        try:
            self.__window.destroy()
        except TclError:
            pass

    def view(self):
        for r in range(self.__rows):
            for c in range(self.__cols):
                bg_color = self.__get_color(r, c)
                # Repaint only changed cells to reduce redraw cost.
                if bg_color != self.__cell_colors_cache[r][c]:
                    self.__canvas.itemconfig(self.__cells[r][c], fill=bg_color)
                    self.__cell_colors_cache[r][c] = bg_color

        self.__window.update_idletasks()  # updates screen
        self.__window.update()

    def __create_widgets(self):
        for r in range(self.__rows):
            row_cells: list[int] = []
            row_colors: list[str] = []
            for c in range(self.__cols):
                color = GAPI_COLORS["VOID"]
                # Convert grid coordinates to canvas pixel rectangle.
                x1 = c * GAPI_BLOCK_SIZE
                y1 = r * GAPI_BLOCK_SIZE
                x2 = x1 + GAPI_BLOCK_SIZE
                y2 = y1 + GAPI_BLOCK_SIZE
                rect_id = self.__canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color,
                    outline="",
                )
                row_cells.append(rect_id)
                row_colors.append(color)
            self.__cells.append(row_cells)
            self.__cell_colors_cache.append(row_colors)

    def __get_color(self, r: int, c: int) -> str:
        if self.is_alive(r, c):
            color = GAPI_COLORS["ALIVE"]
        else:
            if self.was_alive(r, c):
                color = GAPI_COLORS["WAS_ALIVE"]
            else:
                color = GAPI_COLORS["VOID"]
        return color
