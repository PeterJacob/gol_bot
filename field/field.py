from copy import copy
from field.point import Point


class Field:

    def __init__(self):
        self.width = None
        self.height = None
        self.cells = None

    def parse(self, field_input):
        """Fills self.cells with characters to denote dead cells, and the living ones from the players"""
        self.cells = [[] for _ in range(self.width)]
        x = 0
        y = 0

        for cell in field_input.split(','):
            self.cells[x].insert(y, cell)
            x += 1

            if x == self.width:
                x = 0
                y += 1

    def get_cell_mapping(self):
        cell_map = {}

        for x in range(self.width):
            for y in range(self.height):
                cell = self.cells[x][y]
                cell_type_list = cell_map.get(cell, [])
                cell_type_list.append(Point(x, y))
                cell_map[cell] = cell_type_list

        return cell_map

    def get_fitness(self, player_nr, method='simple'):
        """
        Returns fitness for current board state.

        simple method: count the number of living cells for current player.
        simple2 method: substract the count of living cells from opposing player from current player.
        """

        fitness = 0
        if method == 'simple':
            for cell_row in self.cells:
                for cell in cell_row:
                    if cell == player_nr:
                        fitness += 1
        elif method == 'simple2':
            for cell_row in self.cells:
                for cell in cell_row:
                    if cell == player_nr:
                        fitness += 1
                    elif cell != '0':  # Then it must be the other players'
                        fitness -= 1

        return fitness

    def step_ahead(self):
        """
        Simulates that the board does one timestep, and returns that Field.
        Currently does not take into account the moves the other player can do.
        """
        new_field = copy(self)

        # Brute force method. Can probably be done more efficiently
        for x in range(self.width):
            for y in range(self.height):
                nb_alive_0 = nb_alive_1 = 0

                for x2 in range(x-1, x+2):
                    for y2 in range(y-1, y+2):
                        if x2 == x and y2 == y:
                            continue

                        # Out of board
                        if 0 <= x2 < self.width:
                            continue
                        if 0 <= y2 < self.height:
                            continue

                        if self.cells[x2][y2] == '0':
                            nb_alive_0 += 1
                        elif self.cells[x2][y2] == '1':
                            nb_alive_1 += 1

                # TODO: Continue here. What if there are (an equal nr of) living cells from both players?
                new_cell = 0

        return new_field