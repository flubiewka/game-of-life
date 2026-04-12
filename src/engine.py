from dataclasses import dataclass
from src.seed_loader import load_seed


@dataclass(slots=True)
class Cell:
    is_alive: bool
    _x: int
    _y: int


class Engine:
    def __init__(self):
        # Seed loader returns: rows, columns, and coordinates of alive cells.
        self._nrows, self._ncolumns, alive_cells = load_seed()

        self._current_grid = [  # creates "dead" array with dimensions above
            [
                Cell(is_alive=False, _x=row, _y=column)
                for column in range(self._ncolumns)
            ]
            for row in range(self._nrows)
        ]
        self._next_grid = [  # temporary array for logic
            [
                Cell(is_alive=False, _x=row, _y=column)
                for column in range(self._ncolumns)
            ]
            for row in range(self._nrows)
        ]
        self._previous_grid = [  # for trail
            [
                Cell(is_alive=False, _x=row, _y=column)
                for column in range(self._ncolumns)
            ]
            for row in range(self._nrows)
        ]

        for row, col in alive_cells:
            self._current_grid[row][col].is_alive = True

    # public API

    def step(self) -> None:
        self.__analysis()

    def get_dimensions(self) -> tuple[int, int]:
        return self._nrows, self._ncolumns

    def is_alive(self, row: int, col: int) -> bool:
        return self._current_grid[row][col].is_alive

    def was_alive(self, row: int, col: int) -> bool:
        return self._previous_grid[row][col].is_alive

    def __analysis(self) -> None:
        for row in range(self._nrows):
            for col in range(self._ncolumns):
                # Preserve previous generation for trail rendering.
                self._previous_grid[row][col].is_alive = self._current_grid[row][
                    col
                ].is_alive
                alive_neighbour_count = self.__check_neighbours(row, col)

                if alive_neighbour_count < 2 or alive_neighbour_count > 3:
                    self._next_grid[row][col].is_alive = False
                elif alive_neighbour_count == 3:
                    self._next_grid[row][col].is_alive = True
                else:
                    self._next_grid[row][col].is_alive = self._current_grid[row][
                        col
                    ].is_alive

        for row in range(self._nrows):
            for col in range(self._ncolumns):
                # Apply next generation in one pass after all decisions are made.
                self._current_grid[row][col].is_alive = self._next_grid[row][
                    col
                ].is_alive

    def __check_neighbours(self, cell_row: int, cell_col: int) -> int:
        alive_neighbour_count = 0
        for row_index in range(-1, 2):
            for col_index in range(-1, 2):
                if row_index == 0 and col_index == 0:  # if indices == current cell
                    continue

                neighbour_row = (cell_row + row_index) % self._nrows  #! main algorithm
                neighbour_col = (cell_col + col_index) % self._ncolumns
                # Modulo wraps coordinates and makes field edges connected.

                if self._current_grid[neighbour_row][neighbour_col].is_alive:
                    alive_neighbour_count += 1
        return alive_neighbour_count
