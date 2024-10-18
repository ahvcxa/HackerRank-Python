cube = lambda x:x*x*x

def fibonacci(n):
    y = 0
    x = 1
    if n == 1:
        l = [0]
    elif n == 0:
        l = []
    else:
        l = [0, 1]
    for i in range(n - 2):
        z = x + y
        l.append(z)
        y = x
        x = z

    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))