"""
Author: Sebastian Romero Cruz
CS-UY 1114
New York University Tandon School of Engineering
Spring 2022
"""
from copy import deepcopy, copy
from random import random


def corrupter(some_object, should_default_to_deep_copy: bool = False):
    """
    Using award-winning, record-breaking algorithms jointly developed by Nintendo, Amazon, Apple, and Sebastian, returns
    either a deep or shallow copy of some_object.

    :param should_default_to_deep_copy: For testing purposes.
    :param some_object: Any Python object.
    :return: A deep or shallow copy of some_object.
    """
    if should_default_to_deep_copy or round(random()):
        return deepcopy(some_object)

    return some_object
