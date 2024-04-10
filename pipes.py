#> SHAPE DRAWING CHALLENG
#| The goal is to draw an interesting shape using python. I want to use box-drawing
#| characters to create a field of pipes that all join together.
#|
#| chars:
#| 2-ends - ═ ║ ╝ ╗ ╔ ╚
#| 3-ends - ╠ ╣ ╦ ╩
#| 4-ends - ╬  
#|
#| from the top left, loop across the width of the screen and start filling in
#| characters. For each character, check the surrounding cells to see what
#| directions the pipes are facing. Using this information, reduce a list of
#| options to only the valid candidates and pick one at random. 

import shutil
import random

north_facing = {"║", "╝", "╚", "╠", "╣", "╩", "╬", "╨"}
south_facing = {"║", "╗", "╔", "╠", "╣", "╦", "╬", "╥"}
east_facing =  {"═", "╔", "╚", "╠", "╦", "╩", "╬", "╞"}
west_facing =  {"═", "╝", "╗", "╣", "╦", "╩", "╬", "╡" }

class Pipe():
    def __init__(self, north, west):
        self.north = north
        self.west = west
        self.south = bool(random.randint(0,1))
        self.east = bool(random.randint(0,1))

        # print("\n", self.north, self.east, self.south, self.west)
        options = north_facing | east_facing | south_facing | west_facing
        if self.north:
            options.intersection_update(north_facing)
        else:
            options.difference_update(north_facing)

        if self.west:
            options.intersection_update(west_facing)
        else:
            options.difference_update(west_facing)

        if self.east:
            options.intersection_update(east_facing)
        else:
            options.difference_update(east_facing)

        if self.south:
            options.intersection_update(south_facing)
        else:
            options.difference_update(south_facing)
        # we remove north and west facing if they're false as we know they won't
        # get connected


        # print(list(options))
        if len(options) == 0:
            self.char = " "
        else:
            self.char = list(options)[0]

if __name__ == "__main__":
    term_size = shutil.get_terminal_size()
    lines, cols = (term_size.lines, term_size.columns)
    arr = [[Pipe(False, False)]*cols]*lines

    # check each cell on the screen
    for line in range(lines):
        for col in range(cols):
            # check surrounding lines
            # coords = get_neighbours(line, col, (lines, cols))
            try:
                north = arr[line-1][col].south
            except:
                north = False
            try:
                west = arr[line][col-1].east
            except:
                west = False
            new_pipe = Pipe(north, west) # creates a new pipe based on neighbours
            print(new_pipe.char, end="")
            arr[line][col] = new_pipe
        print("")
    print("")

 
