# ARRAYS
from time import time

def compute_average(n):
    data = []
    start = time()

    for k in range(n):
        data.append(None)
    end = time()

    return (end - start) / n

class GameEntry:
    def __init__(self, name, score) -> None:
        self._name = name
        self._score = score

    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._score
    
    def str (self):
        return f"{self._name}, {self._score}"
    
class ScoreBoard:
    def __init__(self, capacity = 10) -> None:
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        return self._board[k]
    
    def str (self):
        return '\n'.join(str(self._board[j]) for j in range(self. n))
    
    def add(self, entry):
        score = entry.get_score()

        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n -1

            while j > 0 and self._board[j - 1].get_score() > score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry

            
