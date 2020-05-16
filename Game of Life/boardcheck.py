class Boardcheck:
    def __init__(self):
        self._grid = [['1','2','3'] ,
                      ['4','5','6'] ,
                      ['7','8','9'] ,
                      ['10','11','12']]
                      
    
    def print_grid(self):
        for row in self._grid:
            print (row)