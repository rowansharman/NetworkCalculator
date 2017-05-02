import numpy


def getDimension():
    inp = input('Enter the number of nodes: ')
    return int(inp)


def getInitialState(dimension):
    s0 = []
    for i in range(dimension):
        inp = input(str.format('Enter initial state of item {}: ', i+1))
        s0.append(float(inp))
    return s0


def getTransitions(dimension):
    transition = []
    for i in range(dimension):
        cols = []
        for j in range(dimension):
            inp = input(str.format('Enter transition from {} to {}: ', j+1, i+1))
            cols.append(float(inp))
        transition.append(cols)
    return transition


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
            print(firstRow)
            print(secondCol)
            dp = dot(firstRow, secondCol)
            print(dp)
            resCol.append(dp)
        res.append(resCol)
    return res


if __name__ == '__main__':
    # dim = getDimension()
    # s0 = getInitialState(dim)
    # t = getTransitions(dim)
    # print(s0)
    # print(t)
    # multiplied = multiply(t, s0)

    first = [[1,3,5],[2,4,6]]
    second = [[1,5],[2,6],[3,7],[4,8]]
    print(first)
    print(second)
    multiplied = multiply(first, second)
    print(multiplied)
