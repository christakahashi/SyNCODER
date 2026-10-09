import inspect
import warnings
from functools import wraps
import typing
from typing import Callable
import numpy as np

__all__ = ["reverse_complement", "_int_to_baseN", "_baseN_to_int", \
           "_check_deprecated", "_is_pow_two", "eeleopard_available"]


def _is_pow_two(n: int):
    """Returns if a number is a power of two."""
    return (n > 0) and ((n & ( ~(n-1) )) == n)
 
def reverse_complement(dna_sequence: str) -> str:
    """Returns the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    reversed_sequence = dna_sequence[::-1]
    reverse_complement_sequence = ''.join(complement[nucleotide] for nucleotide in reversed_sequence)
    return reverse_complement_sequence

def _int_to_baseN(n:int,base:int,length:int=-1)->list[int]:
    """Converts an integer to a base N number in little endian order.

    Args:
        n (int): The integer to be converted.
        base (int): The base of the number system.
        length (int, optional): If specified, the number will be zero padded to this length.

    Returns:
        list[int]: The list of digits representing the base N number.

    """ 

    digits = []
    while n>0:
        n,r = divmod(n,base)
        digits.append(r)
        
    #do zero padding
    while len(digits)<length: 
        digits.append(0)
    return digits

def _baseN_to_int(digits: list[int], base: int) -> int:
    """
    Converts a base N number to an integer using little endian order.

    Args:
        digits (list[int]): The list of digits representing the base N number.
        base (int): The base of the number.

    Returns:
        int: The converted integer value.

    """

    n = 0
    for d in reversed(digits):
        n = n*base + d
    return n


def _check_deprecated(func: Callable[..., typing.Any]) -> Callable[..., typing.Any]:
    """Translate deprecated keyword arguments before calling ``func``."""
    signature = inspect.signature(func)

    @wraps(func)
    def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        positional_arguments = signature.bind_partial(*args).arguments
        replacements = (("words", "alphabet"),
                        ("alternate_words", "alternate_alphabet"))
        for deprecated_name, current_name in replacements:
            if deprecated_name not in kwargs:
                continue
            if current_name in kwargs or current_name in positional_arguments:
                raise TypeError(
                    f"Cannot specify both '{current_name}' and '{deprecated_name}'"
                )
            kwargs[current_name] = kwargs.pop(deprecated_name)
            warnings.warn(
                f"The '{deprecated_name}' parameter is deprecated. Please use "
                f"'{current_name}' instead.",
                DeprecationWarning,
                stacklevel=2,
            )
        return func(*args, **kwargs)

    return wrapper


eeleopard_available = False
try:
    import eeleopard
    eeleopard_available = True
except ImportError: 
    pass

if eeleopard_available:
    class WrappedLeopard(eeleopard.ReedSolomon): # pyright: ignore[reportPossiblyUnboundVariable] .. this is bound >:( 
        def encode(self, message: list[int]):
            temp = super().encode(message)
            ecc = temp[:-self.k]
            data = temp[-self.k:]
            return np.concatenate((data, ecc))

        def decode(self, received, erasures = None,**kwargs): # pyright: ignore[reportIncompatibleMethodOverride]  That's the point
            data = received[:self.k ]
            ecc = received[self.k:]
            orig_codeword = np.concatenate((ecc,data))
            dec_result = super().decode(orig_codeword, erasures,**kwargs)
            return (dec_result.message, dec_result.num_errors,dec_result.error_positions)

    __all__.append( "WrappedLeopard" )