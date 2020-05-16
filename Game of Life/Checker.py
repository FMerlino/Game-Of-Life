def check_next(self, check_row , check_column):
    #how deep the search is:
    search_min = -1
    search_max = 2

    #empty list to append neighbours into.
    neighbour_list = []
    for row in range(search_min,search_max):
        for column in range(search_min,search_max):
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
                neighbour_list.append(self._grid[next_row][next_column])
    return neighbour_list  