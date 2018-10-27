class str(basestring):
    """
    str(object='') -> string

    Return a nice string representation of the object.
    If the argument is a string, the return value is the same object.
    """

    def capitalize(self):
        """ 首字母变大写 """
        """
        S.capitalize() -> string

        Return a copy of the string S with only its first character
        capitalized.
        """
        return ""

    def center(self, width, fillchar=None):
        """ 内容居中，width：总长度；fillchar：空白处填充内容，默认无 """
        """
        S.center(width[, fillchar]) -> string

        Return S centered in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def count(self, sub, start=None, end=None):
        """ 子序列个数 """
        """
        S.count(sub[, start[, end]]) -> int

        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are interpreted
        as in slice notation.
        """
        return 0

    def decode(self, encoding=None, errors=None):
        """ 解码 """
        """
        S.decode([encoding[,errors]]) -> object

        Decodes S using the codec registered for encoding. encoding defaults
        to the default encoding. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
        as well as any other name registered with codecs.register_error that is
        able to handle UnicodeDecodeErrors.
        """
        return object()

    def encode(self, encoding=None, errors=None):
        """ 编码，针对unicode """
        """
        S.encode([encoding[,errors]]) -> object

        Encodes S using the codec registered for encoding. encoding defaults
        to the default encoding. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
        'xmlcharrefreplace' as well as any other name registered with
        codecs.register_error that is able to handle UnicodeEncodeErrors.
        """
        return object()

    def endswith(self, suffix, start=None, end=None):
        """ 是否以 xxx 结束 """
        """
        S.endswith(suffix[, start[, end]]) -> bool

        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, tabsize=None):
        """ 将tab转换成空格，默认一个tab转换成8个空格 """
        """
        S.expandtabs([tabsize]) -> string

        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return ""

    def find(self, sub, start=None, end=None):
        """ 寻找子序列位置，如果没找到，返回 -1 """
        """
        S.find(sub [,start [,end]]) -> int

        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """
        return 0

    def format(*args, **kwargs):  # known special case of str.format
        """ 字符串格式化，动态参数，将函数式编程时细说 """
        """
        S.format(*args, **kwargs) -> string

        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        pass

    def index(self, sub, start=None, end=None):
        """ 子序列位置，如果没找到，报错 """
        S.index(sub[, start[, end]]) -> int

        Like
        S.find()
        but
        raise ValueError
        when
        the
        substring is not found.
        """
        return 0

    def isalnum(self):  
        """
        是否是字母和数字
        """
        """
        S.isalnum() -> bool

        Return
        True if all
        characters in S
        are
        alphanumeric
        and there is at
        least
        one
        character in S, False
        otherwise.
        """
        return False

    def isalpha(self):  
        """
        是否是字母
        """
        """
        S.isalpha() -> bool

        Return
        True if all
        characters in S
        are
        alphabetic
        and there is at
        least
        one
        character in S, False
        otherwise.
        """
        return False

    def isdigit(self):  
        """
        是否是数字
        """
        """
        S.isdigit() -> bool

        Return
        True if all
        characters in S
        are
        digits
        and there is at
        least
        one
        character in S, False
        otherwise.
        """
        return False

    def islower(self):  
        """
        是否小写
        """
        """
        S.islower() -> bool

        Return
        True if all
        cased
        characters in S
        are
        lowercase and there is
        at
        least
        one
        cased
        character in S, False
        otherwise.
        """
        return False

    def isspace(self):  
        """
        S.isspace() -> bool

        Return
        True if all
        characters in S
        are
        whitespace
        and there is at
        least
        one
        character in S, False
        otherwise.
        """
        return False

    def istitle(self):  
        """
        S.istitle() -> bool

        Return
        True if S is a
        titlecased
        string and there is at
        least
        one
        character in S, i.e.uppercase
        characters
        may
        only
        follow
        uncased
        characters and lowercase
        characters
        only
        cased
        ones.Return
        False
        otherwise.
        """
        return False

    def isupper(self):  
        """
        S.isupper() -> bool

        Return
        True if all
        cased
        characters in S
        are
        uppercase and there is
        at
        least
        one
        cased
        character in S, False
        otherwise.
        """
        return False

    def join(self, iterable):  
        """
        连接
        """
        """
        S.join(iterable) -> string

        Return
        a
        string
        which is the
        concatenation
        of
        the
        strings in the
        iterable.The
        separator
        between
        elements is S.
        """
        return ""

    def ljust(self, width, fillchar=None):  
        """
        内容左对齐，右侧填充
        """
        """
        S.ljust(width[, fillchar]) -> string

        Return
        S
        left - justified in a
        string
        of
        length
        width.Padding is
        done
        using
        the
        specified
        fill
        character(default is a
        space).
        """
        return ""

    def lower(self):  
        """
        变小写
        """
        """
        S.lower() -> string

        Return
        a
        copy
        of
        the
        string
        S
        converted
        to
        lowercase.
        """
        return ""

    def lstrip(self, chars=None):  
        """
        移除左侧空白
        """
        """
        S.lstrip([chars]) -> string or unicode

        Return
        a
        copy
        of
        the
        string
        S
        with leading whitespace removed.
        If
        chars is given and not None, remove
        characters in chars
        instead.
        If
        chars is unicode, S
        will
        be
        converted
        to
        unicode
        before
        stripping
        """
        return ""

    def partition(self, sep):  
        """
        分割，前，中，后三部分
        """
        """
        S.partition(sep) -> (head, sep, tail)

        Search
        for the separator sep in S, and return the part before it,
        the
        separator
        itself, and the
        part
        after
        it.If
        the
        separator is not
        found,
        return S and two
        empty
        strings.
        """
        pass

    def replace(self, old, new, count=None):  
        """
        替换
        """
        """
        S.replace(old, new[, count]) -> string

        Return
        a
        copy
        of
        string
        S
        with all occurrences of substring
        old
        replaced
        by
        new.If
        the
        optional
        argument
        count is
        given, only
        the
        first
        count
        occurrences
        are
        replaced.
        """
        return ""

    def rfind(self, sub, start=None, end=None):  
        """
        S.rfind(sub[, start[, end]]) -> int

        Return
        the
        highest
        index in S
        where
        substring
        sub is found,
        such
        that
        sub is contained
        within
        S[start:end].Optional
        arguments
        start and end
        are
        interpreted as in slice
        notation.

        Return - 1
        on
        failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None):  
        """
        S.rindex(sub[, start[, end]]) -> int

        Like
        S.rfind()
        but
        raise ValueError
        when
        the
        substring is not found.
        """
        return 0

    def rjust(self, width, fillchar=None):  
        """
        S.rjust(width[, fillchar]) -> string

        Return
        S
        right - justified in a
        string
        of
        length
        width.Padding is
        done
        using
        the
        specified
        fill
        character(default is a
        space)
        """
        return ""

    def rpartition(self, sep):  
        """
        S.rpartition(sep) -> (head, sep, tail)

        Search
        for the separator sep in S, starting at the end of S, and return
        the
        part
        before
        it, the
        separator
        itself, and the
        part
        after
        it.If
        the
        separator is not found,
        return two
        empty
        strings and S.
        """
        pass

    def rsplit(self, sep=None, maxsplit=None):  
        """
        S.rsplit([sep[, maxsplit]]) -> list
        of
        strings

        Return
        a
        list
        of
        the
        words in the
        string
        S, using
        sep as the
        delimiter
        string, starting
        at
        the
        end
        of
        the
        string and working
        to
        the
        front.If
        maxsplit is given, at
        most
        maxsplit
        splits
        are
        done.If
        sep is not specified or is None, any
        whitespace
        string
        is a
        separator.
        """
        return []

    def rstrip(self, chars=None):  
        """
        S.rstrip([chars]) -> string or unicode

        Return
        a
        copy
        of
        the
        string
        S
        with trailing whitespace removed.
        If
        chars is given and not None, remove
        characters in chars
        instead.
        If
        chars is unicode, S
        will
        be
        converted
        to
        unicode
        before
        stripping
        """
        return ""

    def split(self, sep=None, maxsplit=None):  
        """
        分割， maxsplit最多分割几次
        """
        """
        S.split([sep[, maxsplit]]) -> list
        of
        strings

        Return
        a
        list
        of
        the
        words in the
        string
        S, using
        sep as the
        delimiter
        string.If
        maxsplit is given, at
        most
        maxsplit
        splits
        are
        done.If
        sep is not specified or is None, any
        whitespace
        string is a
        separator and empty
        strings
        are
        removed
        from the result.
        """
        return []

    def splitlines(self, keepends=False):  
        """
        根据换行分割
        """
        """
        S.splitlines(keepends=False) -> list
        of
        strings

        Return
        a
        list
        of
        the
        lines in S, breaking
        at
        line
        boundaries.
        Line
        breaks
        are
        not included in the
        resulting
        list
        unless
        keepends
        is given and true.
        """
        return []

    def startswith(self, prefix, start=None, end=None):  
        """
        是否起始
        """
        """
        S.startswith(prefix[, start[, end]]) -> bool

        Return
        True if S
        starts
        with the specified prefix, False otherwise.
        With
        optional
        start, test
        S
        beginning
        at
        that
        position.
        With
        optional
        end, stop
        comparing
        S
        at
        that
        position.
        prefix
        can
        also
        be
        a
        tuple
        of
        strings
        to
        try.
        """
        return False

    def strip(self, chars=None):  
        """
        移除两段空白
        """
        """
        S.strip([chars]) -> string or unicode

        Return
        a
        copy
        of
        the
        string
        S
        with leading and trailing
            whitespace
            removed.
        If
        chars is given and not None, remove
        characters in chars
        instead.
        If
        chars is unicode, S
        will
        be
        converted
        to
        unicode
        before
        stripping
        """
        return ""

    def swapcase(self):  
        """
        大写变小写，小写变大写
        """
        """
        S.swapcase() -> string

        Return
        a
        copy
        of
        the
        string
        S
        with uppercase characters
        converted
        to
        lowercase and vice
        versa.
        """
        return ""

    def title(self):  
        """
        S.title() -> string

        Return
        a
        titlecased
        version
        of
        S, i.e.words
        start
        with uppercase
            characters, all
            remaining
            cased
            characters
            have
            lowercase.
        """
        return ""

    def translate(self, table, deletechars=None):  
        """
        转换，需要先做一个对应表，最后一个表示删除字符集合
        intab = "aeiou"
        outtab = "12345"
        trantab = maketrans(intab, outtab)
        str = "this is string example....wow!!!"
        print
        str.translate(trantab, 'xm')
        """

        """
        S.translate(table[, deletechars]) -> string

        Return
        a
        copy
        of
        the
        string
        S, where
        all
        characters
        occurring
        in the
        optional
        argument
        deletechars
        are
        removed, and the
        remaining
        characters
        have
        been
        mapped
        through
        the
        given
        translation
        table, which
        must
        be
        a
        string
        of
        length
        256 or None.
        If
        the
        table
        argument is None, no
        translation is applied and
        the
        operation
        simply
        removes
        the
        characters in deletechars.
        """
        return ""

    def upper(self):  
        """
        S.upper() -> string

        Return
        a
        copy
        of
        the
        string
        S
        converted
        to
        uppercase.
        """
        return ""

    def zfill(self, width):  
        """
        方法返回指定长度的字符串，原字符串右对齐，前面填充0。"""
        """
        S.zfill(width) -> string

        Pad
        a
        numeric
        string
        S
        with zeros on the left, to fill a field
        of
        the
        specified
        width.The
        string
        S is never
        truncated.
        """
        return ""

    def _formatter_field_name_split(self, *args, **kwargs): # real signature unknown
        pass

    def _formatter_parser(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, y):  
        """
        x.__add__(y) <= = > x + y
        """
        pass

    def __contains__(self, y):  
        """
        x.__contains__(y) <= = > y in x
        """
        pass

    def __eq__(self, y):  
        """
        x.__eq__(y) <= = > x == y
        """
        pass

    def __format__(self, format_spec):  
        """
        S.__format__(format_spec) -> string

        Return
        a
        formatted
        version
        of
        S as described
        by
        format_spec.
        """
        return ""

    def __getattribute__(self, name):  
        """
        x.__getattribute__('name') <= = > x.name
        """
        pass

    def __getitem__(self, y):  
        """
        x.__getitem__(y) <= = > x[y]
        """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __getslice__(self, i, j):  
        """
        x.__getslice__(i, j) <= = > x[i:j]

        Use
        of
        negative
        indices is not supported.

    """
    pass

def __ge__(self, y):  
    """
    x.__ge__(y) <= = > x >= y
    """
        pass

    def __gt__(self, y):  
        """
    x.__gt__(y) <= = > x > y
    """
        pass

    def __hash__(self):  
        """
    x.__hash__() <= = > hash(x)
    """
        pass

    def __init__(self, string=''): # known special case of str.__init__
        """
    str(object='') -> string

    Return
    a
    nice
    string
    representation
    of
    the
    object.
    If
    the
    argument is a
    string, the
    return value is the
    same
    object.
    # (copied from class doc)
    """
    pass

def __len__(self):  
    """
    x.__len__() <= = > len(x)
    """
        pass

    def __le__(self, y):  
        """
    x.__le__(y) <= = > x <= y
    """
        pass

    def __lt__(self, y):  
        """
    x.__lt__(y) <= = > x < y
    """
        pass

    def __mod__(self, y):  
        """
    x.__mod__(y) <= = > x % y
    """
        pass

    def __mul__(self, n):  
        """
    x.__mul__(n) <= = > x * n
    """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more):  
        """
    T.__new__(S, ...) -> a
    new
    object
    with type S, a subtype of T """
        pass

    def __ne__(self, y):
        """ x.__ne__(y) <= = > x != y """
        pass

    def __repr__(self):
        """ x.__repr__() <= = > repr(x) """
        pass

    def __rmod__(self, y):
        """ x.__rmod__(y) <= = > y % x """
        pass

    def __rmul__(self, n):
        """ x.__rmul__(n) <= = > n * x """
        pass

    def __sizeof__(self):
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __str__(self):
        """ x.__str__() <= = > str(x) """
        pass