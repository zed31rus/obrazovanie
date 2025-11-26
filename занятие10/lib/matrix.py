
class tools():

    def _init_(self):
    
        self.matrixs = {
            'A_3x3': [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],

            'A_4x4': [
                [10, -2, 5, 3],
                [ 0,  7, 1, 8],
                [ 5, -1, 4, 2],
                [ 9,  3, 6, 1]
            ],

            'A_3x4': [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]
            ],

            'A_s': [
                [1, 5, 3],
                [5, 8, 2],
                [3, 2, 9]
            ],

            'A_m': [
                [2, 7, 6],
                [9, 5, 1],
                [4, 3, 8]
            ]
        }
    def getTestMatrix(self, name):
        name = f'A_{name}'
        return self.matrixs.get(name, None)
    
    def matrixFromFile(self, path):
        matrix = []
        with open(path, 'r') as file:
            for line in file:
                row = list(map(float, line.strip().split()))
                matrix.append(row)
        return matrix

#    def matrixToFile(self, path, matrix):

