import time


def timethis(func):
    def wrapper(*args, **kargs):
        start = time.time()
        func(*args, **kargs)
        end = time.time()
        print("%s.%s: %f" % (func.__module__, func.__name__, end - start))

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    countdown(10000000)
