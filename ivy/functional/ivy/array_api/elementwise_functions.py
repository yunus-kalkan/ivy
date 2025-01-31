# local
import ivy
from typing import Union
from ivy.framework_handler import current_framework as _cur_framework


def isfinite(x: Union[ivy.Array, ivy.NativeArray]) -> ivy.Array:
    """
    Tests each element x_i of the input array x to determine if finite (i.e., not NaN and not equal to positive
    or negative infinity).

    :param x: input array. Should have a numeric data type.
    :return: an array containing test results. An element out_i is True if x_i is finite and False otherwise.
             The returned array must have a data type of bool.
    """
    return _cur_framework(x).isfinite(x)


def atanh(x: ivy.Array) -> ivy.Array:
    """
    Calculates an implementation-dependent approximation to the inverse hyperbolic tangent, having domain [-1, +1] and
    codomain [-infinity, +infinity], for each element x_i of the input array x.

    :param x: input array whose elements each represent the area of a hyperbolic sector. Should have a floating-point
    data type.
    :type x: array
    :return: out (array) – an array containing the inverse hyperbolic tangent of each element in x. The returned array
    must have a floating-point data type determined by Type Promotion Rules.
    """
    return _cur_framework(x).atanh(x)
