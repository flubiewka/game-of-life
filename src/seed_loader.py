from src.config import DATA_FILE_PATH


def load_seed(path: str = DATA_FILE_PATH) -> tuple[int, int, list[tuple[int, int]]]:
    with open(path, "r") as file:
        dimensions_tokens = file.readline().split()  # 1st line - dimensions
        if len(dimensions_tokens) < 2:
            raise ValueError("First line must contain two integers: columns and rows")

        # abs() keeps parser tolerant to accidental negative values in file.
        ncolumns = abs(int(dimensions_tokens[0]))
        nrows = abs(int(dimensions_tokens[1]))
        if ncolumns == 0 or nrows == 0:
            raise ValueError("Columns and rows must be greater than zero")

        alive_count_line = file.readline().strip()  # 2nd line - amount of alive cells
        if not alive_count_line:
            raise ValueError("Second line must contain alive cells count")

        alive_cells_count = int(alive_count_line)
        if alive_cells_count < 0:
            raise ValueError("Alive cells count must be non-negative")
        # Hard guard: amount of alive cells cannot exceed grid capacity.
        if alive_cells_count > nrows * ncolumns:
            raise ValueError("Alive cells count cannot exceed grid area")

        alive_cells: list[tuple[int, int]] = []
        for i in range(alive_cells_count):
            coords = file.readline().split()
            if len(coords) < 2:
                raise ValueError(f"Alive cell line {i + 3} must contain row and column")

            row, col = int(coords[0]), int(coords[1])
            # Validate coordinates before adding them to initial seed.
            if not (0 <= row < nrows and 0 <= col < ncolumns):
                raise ValueError(
                    f"Alive cell ({row}, {col}) is out of bounds for grid {nrows}x{ncolumns}"
                )

            alive_cells.append((row, col))

    return nrows, ncolumns, alive_cells
