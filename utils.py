"""Utility functions and helpers for the solution."""

import time
from functools import wraps
from typing import Any, Callable, List, Dict
from logger import logger


def timer(func: Callable) -> Callable:
    """Decorator to measure execution time of a function.
    
    Args:
        func: Function to measure
        
    Returns:
        Wrapped function
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        logger.info(f"{func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper


def memoize(func: Callable) -> Callable:
    """Decorator to cache function results.
    
    Args:
        func: Function to memoize
        
    Returns:
        Wrapped function with caching
    """
    cache: Dict[Any, Any] = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    wrapper.cache = cache
    return wrapper


def read_input(filename: str = None) -> List[str]:
    """Read input from file or stdin.
    
    Args:
        filename: Optional input file name
        
    Returns:
        List of input lines
    """
    try:
        if filename:
            with open(filename, 'r') as f:
                return f.readlines()
        else:
            import sys
            return sys.stdin.readlines()
    except (IOError, OSError) as e:
        logger.error(f"Error reading input: {e}")
        return []


def parse_input(lines: List[str]) -> Any:
    """Parse input lines into usable data.
    
    Args:
        lines: List of input lines
        
    Returns:
        Parsed input data
    """
    return [line.strip() for line in lines if line.strip()]


def format_output(result: Any) -> str:
    """Format solution result for output.
    
    Args:
        result: Solution result
        
    Returns:
        Formatted output string
    """
    return str(result)
