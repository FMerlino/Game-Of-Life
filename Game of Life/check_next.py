def check_next(self, check_row , check_column):
    small_search = -1
    big_search = 2


    next_list = []
    for row in range(small_search, big_search):
        for column in range(small_search, big_search):
            next_row = check_row + row
            next_column = check_column + column 

            valid_neighbour = True

            if (next_row) == check_row and (next_column) == check_column:
                valid_neighbour = False

            if (next_row) < 0 or (next_row) >= self._rows:
                valid_neighbour = False

            if (next_column) < 0 or (next_column) >= self._columns:
                valid_neighbour = False

            if valid_neighbour:
                next_list.append(self._grid[next_row][next_column])
    return next_list  