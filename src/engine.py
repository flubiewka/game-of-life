from dataclasses import dataclass


@dataclass(slots=True)
class Cell:
    is_alive: bool
    _x: int
    _y: int


class Engine:
    def __init__(self):
        with open("data/test.txt", "r") as file:
            line_dimentions = file.readline().split()  # 1st line - dimentions
            self._ncolumns = int(line_dimentions[0])
            self._nrows = int(line_dimentions[1])

            self._arr = [  # creates "dead" array with dimentions above
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

            line_alive = file.readline().strip()  # amount of alive cells
            if line_alive:  # if any are alive
                num_alive = int(line_alive)
                for _ in range(num_alive):  # reviving cells
                    coords = file.readline().split()
                    if coords:
                        row, col = int(coords[0]), int(coords[1])
                        self._arr[row][col].is_alive = True

    def __analysis(self) -> None:
        for row in range(self._nrows):
            for col in range(self._ncolumns):
                self._old[row][col].is_alive = self._arr[row][col].is_alive
                nb = self._check_neighbours(row, col)

                if nb < 2 or nb > 3:
                    self._tmp[row][col].is_alive = False
                elif nb == 3:
                    self._tmp[row][col].is_alive = True
                else:
                    self._tmp[row][col].is_alive = self._arr[row][col].is_alive

        for row in range(self._nrows):
            for col in range(self._ncolumns):
                self._arr[row][col].is_alive = self._tmp[row][col].is_alive

    def step(self) -> None:
        self.__analysis()

    def _check_neighbours(self, cell_row: int, cell_col: int) -> int:
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

    #! public

    def get_dimensions(self) -> tuple[int, int]:
        return self._nrows, self._ncolumns

    def is_alive(self, row: int, col: int) -> bool:
        return self._arr[row][col].is_alive

    def was_alive(self, row: int, col: int) -> bool:
        return self._old[row][col].is_alive
