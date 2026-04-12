from src.config import DATA_FILE_PATH


def load_seed(path: str = DATA_FILE_PATH) -> tuple[int, int, list[tuple[int, int]]]:
    with open(path, "r") as file:
        line_dimensions = file.readline().split()  # 1st line - dimensions
        if len(line_dimensions) < 2:
            raise ValueError("First line must contain two integers: columns and rows")

        ncolumns = abs(int(line_dimensions[0]))
        nrows = abs(int(line_dimensions[1]))
        if ncolumns == 0 or nrows == 0:
            raise ValueError("Columns and rows must be greater than zero")

        line_alive = file.readline().strip()  # 2nd line - amount of alive cells
        if not line_alive:
            raise ValueError("Second line must contain alive cells count")

        num_alive = int(line_alive)
        if num_alive < 0:
            raise ValueError("Alive cells count must be non-negative")
        if num_alive > nrows * ncolumns:
            raise ValueError("Alive cells count cannot exceed grid area")

        alive_cells: list[tuple[int, int]] = []
        for i in range(num_alive):
            coords = file.readline().split()
            if len(coords) < 2:
                raise ValueError(f"Alive cell line {i + 3} must contain row and column")

            row, col = int(coords[0]), int(coords[1])
            if not (0 <= row < nrows and 0 <= col < ncolumns):
                raise ValueError(
                    f"Alive cell ({row}, {col}) is out of bounds for grid {nrows}x{ncolumns}"
                )

            alive_cells.append((row, col))

    return nrows, ncolumns, alive_cells
