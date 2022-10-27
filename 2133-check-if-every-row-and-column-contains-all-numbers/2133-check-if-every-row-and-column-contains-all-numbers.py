import numpy as np
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        return all(len(matrix) == len(set(x)) for x in matrix + list(zip(*matrix)))   
                