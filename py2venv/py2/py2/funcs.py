import numpy as np

def getDelta(a, b, c):
    return b*b-4*a*c

def getVertex(a, b, c):
    x = (-b)*0.5/a
    y = -0.25*getDelta(a,b,c)/a
    return x, y

def getROF(a, b, c):
    if getDelta(a,b,c)<0:
        return "Bez pierwiastków"
    elif getDelta(a, b, c) == 0:
        return getVertex(a, b, c)[0]
    else:
        x1 = getVertex(a, b, c)[0] - np.sqrt(getDelta(a, b, c))
        x2 = getVertex(a, b, c)[0] + np.sqrt(getDelta(a, b, c))
        return x1, x2


print(getDelta(1, 5, 6))
print(getVertex(1, 5, 6))
print(getROF(1, -5, 6))
