from copy import deepcopy
from numpy import linalg


def getDimension():
    inp = input('\nEnter the number of nodes: ')
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
    steps = input('Enter the number of timesteps you would like to simulate or press enter to try another network: ')
    if str.isdigit(steps):
        return int(steps)
    return False


def printMatrix(matrix, rounding):
    print('___')
    for i in range(len(matrix[0])):
        row = '|'
        for j in range(len(matrix)):
            element = round(matrix[j][i], rounding)
            row += str(element) + '\t'
        row += '|'
        print(row)
    print('---')


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
            dp = dot(firstRow, secondCol)
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


def getEigInfo(matrix):
    vals = linalg.eigvals(matrix)
    eigs = []
    for element in vals:
        eigs.append(round(element, 4))
    print('\nEigenvalues:')
    for element in eigs:
        print(element)
    if -1 in vals:
        return 'All initial state vectors will approach a regularly oscillating state'

    num1s = eigs.count(1)
    if num1s == 1:
        return 'All initial state vectors will approach the same equlibrium state'
    elif num1s > 1:
        return 'All initial state vectors will approach some equilibrium state'


if __name__ == '__main__':
    while True:
        dim = getDimension()
        s0 = getInitialState(dim)
        t = getTransitions(dim)
        t = normalize(t)
        if input('Normalize initial state vector? (y/n) ') == 'y':
            s0 = normalize(s0)
        print('\nNormalized transition matrix:')
        printMatrix(t, 2)
        print('\nState vector at time 0:')
        printMatrix(s0, 2)
        print('\n' + getEigInfo(t) + '\n')
        while True:
            steps = getSteps()
            if steps is False:
                break
            finalTransition = exponent(t, steps)
            finalState = multiply(finalTransition, s0)
            print(str.format('\nState vector after {} steps:', steps))
            printMatrix(finalState, 6)
