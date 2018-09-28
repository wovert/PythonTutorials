class int(object):
    """
    int(x=0) -> int or long
    int(x, base=10) -> int or long

    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is floating point, the conversion truncates towards zero.
    If x is outside the integer range, the function returns a long instead.

    If x is not a number or if base is given, then x must be a string or
    Unicode object representing an integer literal in the given base.  The
    literal can be preceded by '+' or '-' and be surrounded by whitespace.
    The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
    interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    """

    def bit_length(self):
        """ 返回表示该数字的时占用的最少位数 """
        """
        int.bit_length() -> int

        Number of bits necessary to represent self in binary.
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        """
        return 0

    def conjugate(self, *args, **kwargs):  # real signature unknown
        """ 返回该复数的共轭复数 """
        """ Returns self, the complex conjugate of any int. """
        pass

    def __abs__(self):
        """ 返回绝对值 """
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, y):
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, y):
        """ x.__and__(y) <==> x&y """
        pass

    def __cmp__(self, y):
        """ 比较两个数大小 """
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __coerce__(self, y):
        """ 强制生成一个元组 """
        """ x.__coerce__(y) <==> coerce(x, y) """
        pass

    def __divmod__(self, y):
        """ 相除，得到商和余数组成的元组 """
        """ x.__divmod__(y) <==> divmod(x, y) """
        pass

    def __div__(self, y):
        """ x.__div__(y) <==> x/y """
        pass

    def __float__(self):
        """ 转换为浮点类型 """
        """ x.__float__() <==> float(x) """
        pass

    def __floordiv__(self, y):
        """ x.__floordiv__(y) <==> x//y """
        pass

    def __format__(self, *args, **kwargs):  # real signature unknown
        pass

    def __getattribute__(self, name):
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getnewargs__(self, *args, **kwargs):  # real signature unknown
        """ 内部调用 __new__方法或创建对象时传入参数使用 """
        pass

    def __hash__(self):
        """如果对象object为哈希表类型，返回对象object的哈希值。哈希值为整数。在字典查找中，哈希值用于快速比较字典的键。两个数值如果相等，则哈希值也相等。"""
        """ x.__hash__() <==> hash(x) """
        pass

    def __hex__(self):
        """ 返回当前数的 十六进制 表示 """
        """ x.__hex__() <==> hex(x) """
        pass

    def __index__(self):
        """ 用于切片，数字无意义 """
        """ x[y:z] <==> x[y.__index__():z.__index__()] """
        pass

    def __init__(self, x, base=10):  # known special case of int.__init__
        """ 构造方法，执行 x = 123 或 x = int(10) 时，自动调用，暂时忽略 """
        """
        int(x=0) -> int or long
        int(x, base=10) -> int or long

        Convert a number or string to an integer, or return 0 if no arguments
        are given.  If x is floating point, the conversion truncates towards zero.
        If x is outside the integer range, the function returns a long instead.

        If x is not a number or if base is given, then x must be a string or
        Unicode object representing an integer literal in the given base.  The
        literal can be preceded by '+' or '-' and be surrounded by whitespace.
        The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
        interpret the base from the string as an integer literal.
        >>> int('0b100', base=0)
        # (copied from class doc)
        """
        pass

    def __int__(self):
        """ 转换为整数 """
        """ x.__int__() <==> int(x) """
        pass

    def __invert__(self):
        """ x.__invert__() <==> ~x """
        pass

    def __long__(self):
        """ 转换为长整数 """
        """ x.__long__() <==> long(x) """
        pass

    def __lshift__(self, y):
        """ x.__lshift__(y) <==> x<<y """
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

    def __nonzero__(self):
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __oct__(self):
        """ 返回改值的 八进制 表示 """
        """ x.__oct__() <==> oct(x) """
        pass

    def __or__(self, y):
        """ x.__or__(y) <==> x|y """
        pass

    def __pos__(self):
        """ x.__pos__() <==> +x """
        pass

    def __pow__(self, y, z=None):
        """ 幂，次方 """
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, y):
        """ x.__radd__(y) <==> y+x """
        pass

    def __rand__(self, y):
        """ x.__rand__(y) <==> y&x """
        pass

    def __rdivmod__(self, y):
        """ x.__rdivmod__(y) <==> divmod(y, x) """
        pass

    def __rdiv__(self, y):
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __repr__(self):
        """转化为解释器可读取的形式 """
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self):
        """转换为人阅读的形式，如果没有适于人阅读的解释形式的话，则返回解释器课阅读的形式"""
        """ x.__str__() <==> str(x) """
        pass

    def __rfloordiv__(self, y):
        """ x.__rfloordiv__(y) <==> y//x """
        pass

    def __rlshift__(self, y):
        """ x.__rlshift__(y) <==> y<<x """
        pass

    def __rmod__(self, y):
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, y):
        """ x.__rmul__(y) <==> y*x """
        pass

    def __ror__(self, y):
        """ x.__ror__(y) <==> y|x """
        pass

    def __rpow__(self, x, z=None):
        """ y.__rpow__(x[, z]) <==> pow(x, y[, z]) """
        pass

    def __rrshift__(self, y):
        """ x.__rrshift__(y) <==> y>>x """
        pass

    def __rshift__(self, y):
        """ x.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, y):
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rtruediv__(self, y):
        """ x.__rtruediv__(y) <==> y/x """
        pass

    def __rxor__(self, y):
        """ x.__rxor__(y) <==> y^x """
        pass

    def __sub__(self, y):
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, y):
        """ x.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args, **kwargs):
        """ 返回数值被截取为整形的值，在整形中无意义 """
        pass

    def __xor__(self, y):
        """ x.__xor__(y) <==> x^y """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ 分母 = 1 """
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ 虚数，无意义 """
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ 分子 = 数字大小 """
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ 实属，无意义 """
    """the real part of a complex number"""

