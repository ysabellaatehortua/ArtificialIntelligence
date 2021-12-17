"""
SudokuSolver.py

Ysabella Atehortua and Natalie Korzh

This file includes all the algorithms implemented to solve sudoku puzzles (CSP, AC3, backtracking),
as well as the set up (creating a puzzle from each line) and main function that runs all the algorithms.
"""
import sys
import copy

class SudokuSolver():


    def __init__(self):
        self.puzzle = None
        self.tuples = None
    
    #checks if puzzle is completed (one digit assigned to each square)
    def isDone(self, puzzle):
        for row in puzzle:
            for element in row:
                if len(element) > 1:
                    return False
        return True

    #parses line from text file and creates 2D array for puzzle
    def createPuzzle(self,line):
        counter = -1
        Puzzle = []
        row = []
        for i in line:
            counter += 1
            if counter % 9 == 0 and counter != 0:
                Puzzle.append(row)
                row = []
            row.insert(counter % 9, i)
        self.puzzle = Puzzle
        return Puzzle
    
    #makes every square in the puzzle a list
    def csp(self):
        for r in range(0, len(self.puzzle)):
            row = self.puzzle[r]
            for c in range(0, len(row)):
                if row[c] == '.':
                    row[c] = [1, 2, 3, 4, 5, 6, 7, 8, 9] #if square is not solved, replace it with domain range 1-9
                else:
                    row[c] = [int(row[c])]
        return self.puzzle
    
    #creates the constraints dictionary by adding all squares in the same row, column and square as the values to each square (key)
    def getNeighbors(self):
        tuples = {}
        for r in range(0, len(self.puzzle)):
            row = self.puzzle[r]
            for c in range(0, len(row)):
                #for every square
                neighbors = []
                for i in range(0, len(row)): #checks rows
                    if i != c:
                        neighbors.append((r, i))
                for i in range(0, len(self.puzzle)): #checks columns
                    if i != r:
                        neighbors.append((i, c))
                row_square = r // 3
                col_square = c // 3
                for x in range(3*row_square, 3*row_square+3):
                    for y in range(3*col_square, 3*col_square+3): #checks squares
                        if x != r and y != c:
                            neighbors.append((x,y))
                tuples[(r,c)] = neighbors
        self.tuples = tuples
        return tuples

    #runs AC3 algorithm by looping through all constraints and running revise to solve the puzzle
    def AC3(self, puzzle):
        rpuzzle = []
        arcs = []
        for square in self.tuples:
            if len(puzzle[square[0]][square[1]]) > 1: #not sure if we need this (i only add a square if it wasnt given / isnt already set)
                for neighbor in self.tuples[square]:
                    arcs.append((square, neighbor))
        while arcs:
            constraint = arcs.pop(0)
            xi = constraint[0]
            xj = constraint[1]
            result = self.revise(xi,xj, puzzle)
            revised = result[0]
            rpuzzle = result[1]
            if revised:
                if len(rpuzzle[xi[0]][xi[1]]) == 0:
                    return rpuzzle
                for neighbor in self.tuples[(xi[0], xi[1])]:
                    arcs.append((neighbor, (xi[0], xi[1])))
        return rpuzzle

    #this function removes integers shared in domains of a squares and each of its constraints
    def revise(self, first, second, puzzle):
        revised = False
        for x in puzzle[first[0]][first[1]]:
            satisfied = False
            for y in puzzle[second[0]][second[1]]:
                if x != y:
                    satisfied = True
            if not satisfied:
                puzzle[first[0]][first[1]].remove(x)
                revised = True
        return revised, puzzle

    #checks if puzzle (as solved so far) does not have a solution (i.e. one of the squares has no possible integers left in domain)
    def checkFail(self, puzzle):
        failure = False
        for row in puzzle:
            for element in row:
                if len(element) == 0:
                    failure = True
        return failure

    #this algorithm tries to solve the puzzle by choosing integers from a squares domain and seeing if the puzzle can be solved with it
    def backtracking(self, puzzle):
        if self.isDone(puzzle):
            printpuzzle(new_puzzle)
            return puzzle
        min_length = 100
        val = list(self.tuples.keys())[0]
        rownum = 0
        colnum = 0
        for row in puzzle:
            for element in row:
                if (len(element) < min_length) and (len(element) > 1): #finding square with smallest size domain (that is not solved i.e. len = 1)
                    min_length = len(element)
                    val = (rownum, colnum)
                colnum += 1
            rownum += 1
            colnum = 0
        
        freq = {}
        for num in puzzle[val[0]][val[1]]:
            for neighbor in self.tuples[val]:
                if num in puzzle[neighbor[0]][neighbor[1]]: #calculating frequencies for each integer in domain of square with smallest domain (how many constraints is it shraed with)
                    if num in freq:
                        freq[num] += 1
                    else:
                        freq[num] = 1
            if num not in freq:
                freq[num] = 0
        lcv = {k:v for k, v in sorted(freq.items(), key = lambda item: item[1])} #sorting frequencies smallest to largest 
        for thing in lcv:
            new_puzzle = copy.deepcopy(puzzle)
            new_puzzle[val[0]][val[1]] = [thing]
            new_puzzle = self.AC3(new_puzzle) #running AC3 with square = integer with smallest frequency left
            if self.isDone(new_puzzle):
                printpuzzle(new_puzzle)
                return new_puzzle
            if not self.checkFail(new_puzzle):
                result = self.backtracking(new_puzzle)
        return new_puzzle

#prints solved puzzle as a line of 81 integers
def printpuzzle(puzzle):
    string = ""
    for line in puzzle:
        for element in line:
            for number in element:
                string += str(number)
    print(string)

#main function, handles reading in input arguments and running algorithms in order 
def main():
    filename = sys.argv[1]
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        #print(counter)
        solver = SudokuSolver()
        puzzle = solver.createPuzzle(line)
        puzzle = solver.csp()
        #print(puzzle)
        solver.getNeighbors()
        solver.AC3(puzzle)
        if not solver.isDone(solver.puzzle):
            #print(solver.puzzle)
            solver.backtracking(solver.puzzle)
        if solver.isDone(solver.puzzle):
            printpuzzle(solver.puzzle)

if __name__ == "__main__":
    main()
