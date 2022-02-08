print ('THE TOWER OF HANOI BY parthivi')

import copy
import sys

TOTAL_DISKS = 5 


SOLVED_TOWER = list(range(TOTAL_DISKS,0,-1))


def main():
    """runs a single game of The Tower of Hanoi."""
    print(
        """THE TOWR OF HANOI,by parthivi    RULES
     #the player can only move one disk at a time.
     #the player can only move disks from the top of the tower
     #the player can never place a larger disk on tpo of a smaller disk
     *more information on https://en.wikipedia.org/wiki/Tower_of_Hanoi
     """

    )
    towers = {"A": copy.copy(SOLVED_TOWER),"B": [], "C": []}

    while True:
        displayTowers(towers)

        fromTower , toTower = getPlayerMove(towers)

        disk = towers[fromTower].pop()
        towers[toTower].append(disk)
        if SOLVED_TOWER in (towers["B"], ["c"]):
            displayTowers(towers)
            print('you have solved the puzzle')
 def getPlayerMove(towers):
     ""           