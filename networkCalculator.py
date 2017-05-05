from copy import deepcopy
from numpy import linalg


def getDimension():
    inp = input('Enter the number of nodes: ')
    return int(inp)


def getInitialState(dimension):
    s0 = []
    for i in range(dimension):
        inp = input(str.format('Enter initial state of item {}: ', i+1))
        s0.append(float(inp))
    return [s0]


def getTransitions(dimension):
    transition = []
    for i in range(dimension):
        cols = []
        for j in range(dimension):
            inp = input(str.format('Enter transition from {} to {}: ', j+1, i+1))
            cols.append(float(inp))
        transition.append(cols)
    return transition


def getSteps():
    steps = input('Enter the number of timesteps you would like to simulate: ')
    return int(steps)


def printMatrix(matrix):
    print('___')
    for i in range(len(matrix[0])):
        row = '|'
        for j in range(len(matrix)):
            row += str(matrix[j][i]) + '\t'
        row += '|'
        print(row)
    print('‾‾‾')


def dot(first, second):
    prod = 0
    for i in range(len(first)):
        prod += first[i] * second[i]
    return prod


def multiply(first, second):
    res = []
    for i in range(len(second)):
        resCol = []
        secondCol = second[i]
        for j in range(len(first[0])):
            firstRow = []
            for k in range(len(first)):
                firstRow.append(first[k][j])
            # print(firstRow)
            # print(secondCol)
            dp = dot(firstRow, secondCol)
            # print(dp)
            resCol.append(dp)
        res.append(resCol)
    return res


def exponent(matrix, power):
    res = deepcopy(matrix)
    for i in range(len(res)):
        for j in range(len(res)):
            if i == j:
                res[i][j] = 1
            else:
                res[i][j] = 0
    for i in range(power):
        res = multiply(matrix, res)
    return(res)


def normalize(matrix):
    res = []
    for i in range(len(matrix)):
        col = []
        tot = 0
        for j in range(len(matrix[i])):
            tot += matrix[i][j]
        for j in range(len(matrix[i])):
            col.append(matrix[i][j] / tot)
        res.append(col)
    return res


if __name__ == '__main__':
    dim = getDimension()
    s0 = getInitialState(dim)
    t = getTransitions(dim)
    t = normalize(t)
    s0 = normalize(s0)
    printMatrix(t)
    printMatrix(s0)
    print(linalg.eigvals(t))
    while True:
        steps = getSteps()
        finalTransition = exponent(t, steps)
        finalState = multiply(finalTransition, s0)
        printMatrix(finalState)
    # multiplied = multiply(t, s0)
    # printMatrix(multiplied)

    # I = [[1,0,0],[0,1,0],[0,0,1]]
    # a = [[1,4,1],[1,0,0],[-1,2,0]]
    # printMatrix(a)
    # b = [[2,3,0],[-1,-2,1]]
    # multiplied = multiply(a,b)
    # printMatrix(multiplied)

    # print('axI =')
    # printMatrix(multiply(a,I))
    #
    # print('axa =')
    # printMatrix(multiply(a,a))
    #
    # print('a^0 =')
    # printMatrix(exponent(a,0))
    #
    # print('a^1 =')
    # printMatrix(exponent(a,1))
    #
    # print('a^2 =')
    # printMatrix(exponent(a,2))
    #
    # print('a^5 =')
    # printMatrix(exponent(a,5))
