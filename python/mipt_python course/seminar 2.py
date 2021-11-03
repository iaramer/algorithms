def minf(l):
    if not l:
        raise Exception("The collection is empty.")
    minel = l[0]
    for i in range(1, len(l)):
        if minel > l[i]:
            minel = l[i]
    return minel


if __name__ == '__main__':
    l = [6, 1, 4, 7, 2]
    act = 1
    res = minf(l)
    assert res == act

    minf([])
