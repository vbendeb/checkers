#!/usr/bin/python

class Checkboard(object):
        def __init__(self):
                self.whites = []
                self.blacks = []
                self.checkers = {}
                for row in range(8):
                        self.checkers[row] = {}
                        for col in range(8):
                                if row < 3:
                                        piece = 'w'
                                        l = self.whites
                                elif row > 4:
                                        piece = 'b'
                                        l = self.blacks
                                else:
                                        continue
                                if not ((col ^ row) & 1):
                                        self.checkers[row][col] = piece
                                        l.append((row, col))
                print self.whites
                print self.blacks

        def __str__(self):
                board = ''
                for row in range(7, -1, -1):
                        for col in range(8):
                                board += self.checkers[row].get(col, '.')
                        board += '\n'
                return board


        def move(self, color):
                if color == 'w':
                        l = self.whites
                        dir = 1
                else:
                        l = self.blacks
                        dir = -1
                for row, col in l:
                        nr = row + dir
                        if row >= 0 and row < 8:
                                nc = col - 1
                                if nc < 0:
                                        continue
                                if nc not in self.checkers[nr]:
                                        self.checkers[nr][nc] = self.checkers[row][col]
                                        del self.checkers[row][col]
                                        return

                                nc = col + 1
                                if nc > 7:
                                        continue
                                if nc not in self.checkers[nr]:
                                        self.checkers[nr][nc] = self.checkers[row][col]
                                        del self.checkers[row][col]
                                        return


cb = Checkboard()
print cb
cb.move('w')
print cb
