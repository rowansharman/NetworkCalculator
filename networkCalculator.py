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
            inp = input(str.format('Enter transition from {} to {}: ', i+1, j+1))
            cols.append(float(inp))
        transition.append(cols)
    return transition


def multiply(transition, initial):
    res = []
    for i in range(len(initial)):
        added = 0
        for j in range(len(initial)):
            added += transition[j][i] * initial[j]
        res.append(added)
    return res


if __name__ == '__main__':
    dim = getDimension()
    s0 = getInitialState(dim)
    t = getTransitions(dim)
    print(s0)
    print(t)
    multiplied = multiply(t, s0)
    print(multiplied)
