
import os

def clamp(val, lower, upper):
    """ val if it's between lower and upper, else the closest of the two"""
    return max(min(val, upper), lower)

def get(collection, i, default=None):
    """ Get an element in an indexed collection, or the default in case the index is out of bounds """
    if i < 0 or i >= len(collection):
        return default
    return collection[i]
