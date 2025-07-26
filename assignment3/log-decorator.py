# Task 1: Writing and Testing a Decorator
import logging 
from functools import wraps 

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pos_args = args if args else "none"
        kw_args = kwargs if kwargs else "none"
        res = func(*args, **kwargs)
        log_msg = (
            f"function: {func.__name__}\n"
            f"positional parameters: {pos_args}\n"
            f"keyword parameters: {kw_args}\n"
            f"return: {res}\n"
        )
        logger.info(log_msg)
        return res 
    return wrapper 

@logger_decorator 
def greet():
    return ("Hello, World!")

@logger_decorator
def return_true(*args):
    return True 

@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    greet()
    return_true("a", "b")
    return_decorator(name="Someone", location="NY", language="Python")