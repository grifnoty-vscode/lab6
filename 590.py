pos = input()
cols = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
knight_col = cols[pos[0]]
knight_row = 8 - int(pos[1])
moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
attacked = set()

for dr, dc in moves:
    r, c = knight_row + dr, knight_col + dc
    if 0 <= r < 8 and 0 <= c < 8:
        attacked.add((r, c))

for r in range(8):
    row_cells = []
    for c in range(8):
        if (r, c) == (knight_row, knight_col):
            row_cells.append('K')
        elif (r, c) in attacked:
            row_cells.append('*')
        else:
            row_cells.append('.')
    print(' '.join(row_cells))