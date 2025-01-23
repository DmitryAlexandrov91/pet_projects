"""Утилиты проекта haddan  parser."""


def divide_dict_in_half(dct):
    keys = list(dct.keys())
    mid_point = len(keys) // 2
    first_half_keys = keys[:mid_point]
    second_half_keys = keys[mid_point:]
    first_half = {k: dct[k] for k in first_half_keys}
    second_half = {k: dct[k] for k in second_half_keys}
    return first_half, second_half
