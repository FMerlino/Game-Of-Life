from Cell_class import Cell
from random import randint

class Grid:
    def __init__(self , rows , columns):
        self._rows = rows
        self._columns = columns   
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]
        self._create_grid()

    def draw_grid(self):
        print('\n'*10)
        print('printing grid')
        for row in self._grid:
            for column in row:
                print (column.get_print_character(),end='')
            print ()

    def _create_grid(self):
        for row in self._grid:
            for column in row:
                #there is a 33% chance the cells spawn alive.
                chance_number = randint(0,2)
                if chance_number == 1:
                    column.set_alive()