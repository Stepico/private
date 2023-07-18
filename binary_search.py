def binary_search(data, value):
    lo, hi = 0, len(data) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if data[mid] == value:
            return mid

        if data[mid] > value:
            hi = mid - 1
        else:
            lo = mid + 1

    return False


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
