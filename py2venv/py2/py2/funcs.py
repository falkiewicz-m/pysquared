import numpy as np
import argparse

parser = argparse.ArgumentPasser(description='Processing maths in parabolic function')
parser.add_argument('Coefficients', metavar='a, b, c', nargs = 3, help='Input for coefficients')

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


print(getDelta(d, e, f))
print(getVertex(d, e, f))
print(getROF(d, e, f))
