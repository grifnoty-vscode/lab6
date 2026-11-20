pos = input("Введіть позицію ферзя (наприклад, d5): ")
cols = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
queen_col = cols[pos[0]]
queen_row = 8 - int(pos[1])

for r in range(8):
    row_cells = []
    for c in range(8):
        if r == queen_row and c == queen_col:
            row_cells.append('Q')
        elif r == queen_row or c == queen_col or abs(r - queen_row) == abs(c - queen_col):
            row_cells.append('*')
        else:
            row_cells.append('.')
    print(' '.join(row_cells))