from typing import Any


def callLimit(limit: int):

    count = 0

    def callLimiter(function):

        def limit_function(*args: Any, **kwds: Any):
            nonlocal count

            if count >= limit:
                print(f"Error: Function at {function} call too many times")
                return
            else:
                count += 1
                return function(*args, **kwds)

        return limit_function

    return callLimiter