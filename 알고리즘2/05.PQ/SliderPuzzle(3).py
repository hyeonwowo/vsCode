import copy
import random
from queue import PriorityQueue

class Board:
    def __init__(self, tiles):  # Constructor
        self.n = len(tiles)
        self.tiles = copy.deepcopy(tiles)
        self.twinBoard = None

        # Compute Hamming distance
        self.hammingDistance = 0
        goal = 0
        for rowId, row in enumerate(tiles):
            for colId, t in enumerate(row):
                goal += 1
                if t == 0:
                    continue
                if t != goal:
                    self.hammingDistance += 1

        # Compute Manhattan distance
        self.manhattanDistance = 0
        for rowId, row in enumerate(tiles):
            for colId, t in enumerate(row):
                if t == 0:
                    continue
                goalRow, goalCol = (t - 1) // self.n, (t - 1) % self.n
                self.manhattanDistance += abs(rowId - goalRow) + abs(colId - goalCol)

        # Find the empty tile and store its location in (self.rowZero, self.colZero)
        self.rowZero, self.colZero = None, None
        for rowId, row in enumerate(self.tiles):
            for colId, t in enumerate(row):
                if t == 0:
                    self.rowZero, self.colZero = rowId, colId
        assert self.rowZero is not None and self.colZero is not None

    def __str__(self):
        return '\n'.join([' '.join(f'{t:2d}' for t in row) for row in self.tiles]) + '\n'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Board) and self.tiles == other.tiles

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.tiles))

    def __lt__(self, other):
        return self.manhattan() < other.manhattan()

    def hamming(self):
        return self.hammingDistance

    def manhattan(self):
        return self.manhattanDistance

    def dimension(self):
        return self.n

    def isGoal(self):
        return self.hammingDistance == 0

    def neighbors(self):
        neighborList = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        for dr, dc in directions:
            newRow, newCol = self.rowZero + dr, self.colZero + dc
            if 0 <= newRow < self.n and 0 <= newCol < self.n:
                newTiles = copy.deepcopy(self.tiles)
                newTiles[self.rowZero][self.colZero], newTiles[newRow][newCol] = newTiles[newRow][newCol], 0
                neighborList.append(Board(newTiles))
        return neighborList

    def twin(self):
        if self.twinBoard is None:
            for row in range(self.n):
                for col in range(self.n - 1):
                    if self.tiles[row][col] != 0 and self.tiles[row][col + 1] != 0:
                        newTiles = copy.deepcopy(self.tiles)
                        newTiles[row][col], newTiles[row][col + 1] = newTiles[row][col + 1], newTiles[row][col]
                        self.twinBoard = Board(newTiles)
                        return self.twinBoard
        return self.twinBoard


def solveManhattan(initialBoard):
    return None


def solveNprint(initialBoard, solveFunction=solveManhattan):
    solution = solveFunction(initialBoard)
    if solution is not None:
        print(f"Solvable in {len(solution) - 1} moves")
        for board in solution:
            print(board)
    else:
        print("Unsolvable")


def correctnessTest(func, input, expected_len, expected_output, correct):
    print(f"{func.__name__}(\n{input})")
    output = func(input)
    if output is not None and isinstance(output, list):
        if len(output) == expected_len:
            if expected_output is None:
                print("Pass")
            elif expected_output == output:
                print("Pass")
            else:
                print(f"Fail - the output does not match the expected output")
                correct = False
        else:
            print(f"Fail - length of output {len(output)} is not equal to {expected_len}")
            correct = False
    else:
        print(f"Fail - output is NOT a list")
        correct = False
    print()
    return correct

if __name__ == "__main__":
    '''
    For visual inspection
    '''
    # Solvable in 0 move (already solved)
    b0 = Board([[1,2,3],[4,5,6],[7,8,0]])    
    solveNprint(b0)
    
    # Solvable in 4 moves
    b4 = Board([[0,1,3],[4,2,5],[7,8,6]])
    solveNprint(b4)  

    
    '''
    Unit Test
    '''    
    print("Correctness test for solveManhattan()")
    print("For each test case, if your answer does not appear within 10 seconds, then consider that you failed the case")
    print()
    correct = True

    b0 = Board([[1,2,3],[4,5,6],[7,8,0]])
    correct = correctnessTest(solveManhattan, b0, 1, [b0], correct)

    b4 = Board([[0,1,3],[4,2,5],[7,8,6]])
    b41 = Board([[1,0,3],[4,2,5],[7,8,6]])
    b42 = Board([[1,2,3],[4,0,5],[7,8,6]])
    b43 = Board([[1,2,3],[4,5,0],[7,8,6]])
    b44 = Board([[1,2,3],[4,5,6],[7,8,0]])
    correct = correctnessTest(solveManhattan, b4, 5, [b4, b41, b42, b43, b44], correct)

    b4_5 = Board([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 0, 14, 15], [16, 17, 13, 19, 20], [21, 22, 18, 23, 24]])
    b4_5_1 = Board([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 0, 19, 20], [21, 22, 18, 23, 24]])
    b4_5_2 = Board([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 0, 23, 24]])
    b4_5_3 = Board([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 0, 24]])
    b4_5_4 = Board([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]])
    correct = correctnessTest(solveManhattan, b4_5, 5, [b4_5, b4_5_1, b4_5_2, b4_5_3, b4_5_4], correct)
    
    b3_2 = Board([[3, 1], [0, 2]])
    b3_2_1 = Board([[0, 1], [3, 2]])
    b3_2_2 = Board([[1, 0], [3, 2]])
    b3_2_3 = Board([[1, 2], [3, 0]])
    correct = correctnessTest(solveManhattan, b3_2, 4, [b3_2, b3_2_1, b3_2_2, b3_2_3], correct)    

    b4_10 = Board([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                      [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                      [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                      [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                      [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
                      [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                      [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                      [81, 82, 83, 84, 85, 86, 0, 87, 89, 90],
                      [91, 92, 93, 94, 95, 96, 97, 88, 98, 99]])
    b4_10_1 = Board([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                        [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                        [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                        [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
                        [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                        [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                        [81, 82, 83, 84, 85, 86, 87, 0, 89, 90],
                        [91, 92, 93, 94, 95, 96, 97, 88, 98, 99]])
    b4_10_2 = Board([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                        [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                        [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                        [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
                        [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                        [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                        [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
                        [91, 92, 93, 94, 95, 96, 97, 0, 98, 99]])
    b4_10_3 = Board([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                        [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                        [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                        [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
                        [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                        [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                        [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
                        [91, 92, 93, 94, 95, 96, 97, 98, 0, 99]])
    b4_10_4 = Board([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                        [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                        [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                        [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
                        [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                        [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                        [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
                        [91, 92, 93, 94, 95, 96, 97, 98, 99, 0]])
    correct = correctnessTest(solveManhattan, b4_10, 5, [b4_10, b4_10_1, b4_10_2, b4_10_3, b4_10_4], correct)

    b6_4 = Board([[0, 1, 2, 3], [5, 6, 7, 4], [9, 10, 11, 8], [13, 14, 15, 12]])
    correct = correctnessTest(solveManhattan, b6_4, 7, None, correct)

    b12_3 = Board([[0, 1, 2], [4, 5, 3], [6, 7, 8]])
    correct = correctnessTest(solveManhattan, b12_3, 13, None, correct)

    b14 = Board([[8,1,3],[4,0,2],[7,6,5]])
    correct = correctnessTest(solveManhattan, b14, 15, None, correct)

    b24 = Board([[3,2,1],[6,5,4],[0,7,8]])
    correct = correctnessTest(solveManhattan, b24, 25, None, correct)
    
    print("This case takes several seconds, longer than the other cases")
    b34_4 = Board([[0, 1, 2, 3], [5, 6, 7, 4], [8, 9, 10, 11], [12, 13, 14, 15]])
    correct = correctnessTest(solveManhattan, b34_4, 35, None, correct)
    
