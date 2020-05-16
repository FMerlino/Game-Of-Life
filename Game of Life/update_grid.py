def update_grid(self):
    print ('updating grid')
    cells_alive = []
    cells_killed = []

    for row in range(len(self._grid)):
        for column in range(len(self._grid[row])):
            
            #check neighbour pr. square:
            check_next = self.check_next(row , column)

            living_neighbours_count = []

            for next_cell in check_next:
                #check live status for neighbour_cell:
                if next_cell.is_alive():
                    living_neighbours_count.append(next_cell)

            cell_object = self._grid[row][column]
            status_main_cell = cell_object.is_alive()

            if status_main_cell == True:
                if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                    cells_killed.append(cell_object)

                if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                    cells_alive.append(cell_object)

            else:
                if len(living_neighbours_count) == 3:
                    cells_alive.append(cell_object)

    #sett cell statuses
    for cell_items in cells_alive:
        cell_items.set_alive()

    for cell_items in cells_killed:
        cell_items.set_dead()