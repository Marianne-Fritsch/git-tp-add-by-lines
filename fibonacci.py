"""
la suite de fibonacci
"""
from functools import cache

@cache
def fibo_cached(n):
    """
    # une implémentation naïve et inefficace
    """
    if n <= 1:
        return n
    else:
        return fibo_cached(n-1) + fibo_cached(n-2)
