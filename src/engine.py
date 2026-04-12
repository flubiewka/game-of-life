from dataclasses import dataclass
from src.seed_loader import load_seed


@dataclass(slots=True)
class Cell:
    is_alive: bool
    _x: int
    _y: int


class Engine:
    def __init__(self):
        self._nrows, self._ncolumns, alive_cells = load_seed()

        self._arr = [  # creates "dead" array with dimensions above
            [
                Cell(is_alive=False, _x=row, _y=column)
                for column in range(self._ncolumns)
            ]
            for row in range(self._nrows)
        ]
        self._tmp = [  # temporary array for logic
            [
                Cell(is_alive=False, _x=row, _y=column)
                for column in range(self._ncolumns)
            ]
            for row in range(self._nrows)
        ]
        self._old = [  # for trail
            [
                Cell(is_alive=False, _x=row, _y=column)
                for column in range(self._ncolumns)
            ]
            for row in range(self._nrows)
        ]

        for row, col in alive_cells:
            self._arr[row][col].is_alive = True

    # public API

    def step(self) -> None:
        self.__analysis()

    def get_dimensions(self) -> tuple[int, int]:
        return self._nrows, self._ncolumns

    def is_alive(self, row: int, col: int) -> bool:
        return self._arr[row][col].is_alive

    def was_alive(self, row: int, col: int) -> bool:
        return self._old[row][col].is_alive

    def __analysis(self) -> None:
        for row in range(self._nrows):
            for col in range(self._ncolumns):
                self._old[row][col].is_alive = self._arr[row][col].is_alive
                nb = self.__check_neighbours(row, col)

                if nb < 2 or nb > 3:
                    self._tmp[row][col].is_alive = False
                elif nb == 3:
                    self._tmp[row][col].is_alive = True
                else:
                    self._tmp[row][col].is_alive = self._arr[row][col].is_alive

        for row in range(self._nrows):
            for col in range(self._ncolumns):
                self._arr[row][col].is_alive = self._tmp[row][col].is_alive

    def __check_neighbours(self, cell_row: int, cell_col: int) -> int:
        nb_amount = 0
        for row_index in range(-1, 2):
            for col_index in range(-1, 2):
                if row_index == 0 and col_index == 0:  # if indices == current cell
                    continue

                r = (cell_row + row_index) % self._nrows  #! main algorithm
                c = (cell_col + col_index) % self._ncolumns

                if self._arr[r][c].is_alive:
                    nb_amount += 1
        return nb_amount
