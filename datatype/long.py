class long(object):
    """
    long(x=0) -> long
    long(x, base=10) -> long

    Convert a number or string to a long integer, or return 0L if no arguments
    are given.  If x is floating point, the conversion truncates towards zero.

    If x is not a number or if base is given, then x must be a string or
    Unicode object representing an integer literal in the given base.  The
    literal can be preceded by '+' or '-' and be surrounded by whitespace.
    The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
    interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4L
    """

    def bit_length(self):  # real signature unknown; restored from __doc__
        """
        long.bit_length() -> int or long

        Number of bits necessary to represent self in binary.
        >>> bin(37L)
        '0b100101'
        >>> (37L).bit_length()
        """
        return 0

    def conjugate(self, *args, **kwargs):  # real signature unknown
        """ Returns self, the complex conjugate of any long. """
        pass

    def __abs__(self):  # real signature unknown; restored from __doc__
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, y):  # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, y):  # real signature unknown; restored from __doc__
        """ x.__and__(y) <==> x&y """
        pass

    def __cmp__(self, y):  # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __coerce__(self, y):  # real signature unknown; restored from __doc__
        """ x.__coerce__(y) <==> coerce(x, y) """
        pass

    def __divmod__(self, y):  # real signature unknown; restored from __doc__
        """ x.__divmod__(y) <==> divmod(x, y) """
        pass

    def __div__(self, y):  # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
        pass

    def __float__(self):  # real signature unknown; restored from __doc__
        """ x.__float__() <==> float(x) """
        pass

    def __floordiv__(self, y):  # real signature unknown; restored from __doc__
        """ x.__floordiv__(y) <==> x//y """
        pass

    def __format__(self, *args, **kwargs):  # real signature unknown
        pass

    def __getattribute__(self, name):  # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getnewargs__(self, *args, **kwargs):  # real signature unknown
        pass

    def __hash__(self):  # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __hex__(self):  # real signature unknown; restored from __doc__
        """ x.__hex__() <==> hex(x) """
        pass

    def __index__(self):  # real signature unknown; restored from __doc__
        """ x[y:z] <==> x[y.__index__():z.__index__()] """
        pass

    def __init__(self, x=0):  # real signature unknown; restored from __doc__
        pass

    def __int__(self):  # real signature unknown; restored from __doc__
        """ x.__int__() <==> int(x) """
        pass

    def __invert__(self):  # real signature unknown; restored from __doc__
        """ x.__invert__() <==> ~x """
        pass

    def __long__(self):  # real signature unknown; restored from __doc__
        """ x.__long__() <==> long(x) """
        pass

    def __lshift__(self, y):  # real signature unknown; restored from __doc__
        """ x.__lshift__(y) <==> x<<y """
        pass

    def __mod__(self, y):  # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, y):  # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self):  # real signature unknown; restored from __doc__
        """ x.__neg__() <==> -x """
        pass

    @staticmethod  # known case of __new__
    def __new__(S, *more):  # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __nonzero__(self):  # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __oct__(self):  # real signature unknown; restored from __doc__
        """ x.__oct__() <==> oct(x) """
        pass

    def __or__(self, y):  # real signature unknown; restored from __doc__
        """ x.__or__(y) <==> x|y """
        pass

    def __pos__(self):  # real signature unknown; restored from __doc__
        """ x.__pos__() <==> +x """
        pass

    def __pow__(self, y, z=None):  # real signature unknown; restored from __doc__
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, y):  # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rand__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rand__(y) <==> y&x """
        pass

    def __rdivmod__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rdivmod__(y) <==> divmod(y, x) """
        pass

    def __rdiv__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __repr__(self):  # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rfloordiv__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rfloordiv__(y) <==> y//x """
        pass

    def __rlshift__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rlshift__(y) <==> y<<x """
        pass

    def __rmod__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __ror__(self, y):  # real signature unknown; restored from __doc__
        """ x.__ror__(y) <==> y|x """
        pass

    def __rpow__(self, x, z=None):  # real signature unknown; restored from __doc__
        """ y.__rpow__(x[, z]) <==> pow(x, y[, z]) """
        pass

    def __rrshift__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rrshift__(y) <==> y>>x """
        pass

    def __rshift__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rtruediv__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rtruediv__(y) <==> y/x """
        pass

    def __rxor__(self, y):  # real signature unknown; restored from __doc__
        """ x.__rxor__(y) <==> y^x """
        pass

    def __sizeof__(self, *args, **kwargs):  # real signature unknown
        """ Returns size in memory, in bytes """
        pass

    def __str__(self):  # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __sub__(self, y):  # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, y):  # real signature unknown; restored from __doc__
        """ x.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args, **kwargs):  # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, y):  # real signature unknown; restored from __doc__
        """ x.__xor__(y) <==> x^y """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""