def reshape_matrix(a, new_shape):
    rows = len(a)
    cols = len(a[0])

    n_rows = new_shape[0]
    n_cols = new_shape[1]

    if rows * cols != n_rows * n_cols:
        return []

    elements = []

    for row in a:
        for value in row:
            elements.append(value)

    reshaped_matrix = []

    for r in range(n_rows):
        row = []

        for c in range(n_cols):
            row.append(elements[r * n_cols + c])

        reshaped_matrix.append(row)

    return reshaped_matrix