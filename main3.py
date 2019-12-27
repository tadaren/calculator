import math

def log(m, e):
    return math.log(m, e)

def mod(x, p):
    return x % p

def pow(x, y):
    return math.pow(x, y)

def pi():
    return math.pi

def e():
    return math.e

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def asin(x):
    return math.asin(x)

def acos(x):
    return math.acos(x)

def atan(x):
    return math.atan(x)

def factorial(x):
    out = 1
    for i in range(1, x):
        out *= i
    return out

def main():
    Ans = 0
    while True:
        print('> ', end='')
        line = input()
        if line == 'exit':
            break
        Ans = eval(line.replace('pi', 'pi()').replace('e', 'e()'))
        print('=', Ans)

if __name__ == "__main__":
    main()