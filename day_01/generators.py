def Counter(stop):
    i = 0
    while i < stop:
        yield i
        i += 1

c = Counter(10)

next(c)
next(c)
next(c)
next(c)
next(c)
