def average(array):
    uniqe_arr = set(array)

    return sum(uniqe_arr) / len(uniqe_arr)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
