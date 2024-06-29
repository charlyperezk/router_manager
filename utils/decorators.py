import time
from functools import wraps


def time_control(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        difference = end_time - start_time
        if difference > 1:
            print(f"The {func.__name__} execution time was: {difference}")
        else:
            print(f"The {func.__name__} execution time was less than 1 second.")
        return result
    return wrapper

def logs(denomination):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            print(f"Executing {func.__name__} for {denomination}")
            result = await func(*args, **kwargs)
            print(f"Executed {func.__name__} for {denomination}")
            return result
        return wrapper
    return decorator
