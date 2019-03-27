class float(object):
    """
    float(x) -> floating point number

    Convert a string or number to a floating point number, if possible.
    """

    def as_integer_ratio(self):
        """ 获取改值的最简比 """
        """
        float.as_integer_ratio() -> (int, int)

        Return a pair of integers, whose ratio is exactly equal to the original
        float and with a positive denominator.
        Raise OverflowError on infinities and a ValueError on NaNs.

        >>> (10.0).as_integer_ratio()
        (10, 1)
        >>> (0.0).as_integer_ratio()
        (0, 1)
        >>> (-.25).as_integer_ratio()
        (-1, 4)
        """
        pass

    def conjugate(self, *args, **kwargs):  # real signature unknown
        """ Return self, the complex conjugate of any float. """
        pass

    def fromhex(self, string):
        """ 将十六进制字符串转换成浮点型 """
        """
        float.fromhex(string) -> float

        Create a floating-point number from a hexadecimal string.
        >>> float.fromhex('0x1.ffffp10')
        2047.984375
        >>> float.fromhex('-0x1p-1074')
        -4.9406564584124654e-324
        """
        return 0.0

    def hex(self):
        """ 返回当前值的 16 进制表示 """
        """
        float.hex() -> string

        Return a hexadecimal representation of a floating-point number.
        >>> (-0.1).hex()
        '-0x1.999999999999ap-4'
        >>> 3.14159.hex()
        '0x1.921f9f01b866ep+1'
        """
        return ""

    def is_integer(self, *args, **kwargs):  # real signature unknown
        """ Return True if the float is an integer. """
        pass

    def __abs__(self):
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, y):
        """ x.__add__(y) <==> x+y """
        pass

    def __coerce__(self, y):
        """ x.__coerce__(y) <==> coerce(x, y) """
        pass

    def __divmod__(self, y):
        """ x.__divmod__(y) <==> divmod(x, y) """
        pass

    def __div__(self, y):
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, y):
        """ x.__eq__(y) <==> x==y """
        pass

    def __float__(self):
        """ x.__float__() <==> float(x) """
        pass

    def __floordiv__(self, y):
        """ x.__floordiv__(y) <==> x//y """
        pass

    def __format__(self, format_spec):
        """
        float.__format__(format_spec) -> string

        Formats the float according to format_spec.
        """
        return ""

    def __getattribute__(self, name):
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getformat__(self, typestr):
        """
        float.__getformat__(typestr) -> string

        You probably don't want to use this function.  It exists mainly to be
        used in Python's test suite.

        typestr must be 'double' or 'float'.  This function returns whichever of
        'unknown', 'IEEE, big-endian' or 'IEEE, little-endian' best describes the
        format of floating point numbers used by the C type named by typestr.
        """
        return ""

    def __getnewargs__(self, *args, **kwargs):  # real signature unknown
        pass

    def __ge__(self, y):
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y):
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self):
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, x):
        pass

    def __int__(self):
        """ x.__int__() <==> int(x) """
        pass

    def __le__(self, y):
        """ x.__le__(y) <==> x<=y """
        pass

    def __long__(self):
        """ x.__long__() <==> long(x) """
        pass

    def __lt__(self, y):
        """ x.__lt__(y) <==> x<y """
        pass

    def __mod__(self, y):
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, y):
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self):
        """ x.__neg__() <==> -x """
        pass

    @staticmethod  # known case of __new__
    def __new__(S, *more):
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y):
        """ x.__ne__(y) <==> x!=y """
        pass

    def __nonzero__(self):
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __pos__(self):
        """ x.__pos__() <==> +x """
        pass

    def __pow__(self, y, z=None):
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, y):
        """ x.__radd__(y) <==> y+x """
        pass

    def __rdivmod__(self, y):
        """ x.__rdivmod__(y) <==> divmod(y, x) """
        pass

    def __rdiv__(self, y):
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __repr__(self):
        """ x.__repr__() <==> repr(x) """
        pass

    def __rfloordiv__(self, y):
        """ x.__rfloordiv__(y) <==> y//x """
        pass

    def __rmod__(self, y):
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, y):
        """ x.__rmul__(y) <==> y*x """
        pass

    def __rpow__(self, x, z=None):
        """ y.__rpow__(x[, z]) <==> pow(x, y[, z]) """
        pass

    def __rsub__(self, y):
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rtruediv__(self, y):
        """ x.__rtruediv__(y) <==> y/x """
        pass

    def __setformat__(self, typestr, fmt):
        """
        float.__setformat__(typestr, fmt) -> None

        You probably don't want to use this function.  It exists mainly to be
        used in Python's test suite.

        typestr must be 'double' or 'float'.  fmt must be one of 'unknown',
        'IEEE, big-endian' or 'IEEE, little-endian', and in addition can only be
        one of the latter two if it appears to match the underlying C reality.

        Override the automatic determination of C-level floating point type.
        This affects how floats are converted to and from binary strings.
        """
        pass

    def __str__(self):
        """ x.__str__() <==> str(x) """
        pass

    def __sub__(self, y):
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, y):
        """ x.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args, **kwargs):  # real signature unknown
        """ Return the Integral closest to x between 0 and x. """
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""