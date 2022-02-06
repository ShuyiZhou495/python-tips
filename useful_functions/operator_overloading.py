class point:
    """
    +	__add__(self, other)
    –	__sub__(self, other)
    *	__mul__(self, other)
    /	__truediv__(self, other)
    //	__floordiv__(self, other)
    %	__mod__(self, other)
    **	__pow__(self, other)
    >>	__rshift__(self, other)
    <<	__lshift__(self, other)
    &	__and__(self, other)
    |	__or__(self, other)
    ^	__xor__(self, other)


    <	__lt__(self, other)
    >	__gt__(self, other)
    <=	__le__(self, other)
    >=	__ge__(self, other)
    ==	__eq__(self, other)
    !=	__ne__(self, other)

    -=	__isub__(self, other)
    +=	__iadd__(self, other)
    *=	__imul__(self, other)
    /=	__idiv__(self, other)
    //=	__ifloordiv__(self, other)
    %=	__imod__(self, other)
    **=	__ipow__(self, other)
    >>=	__irshift__(self, other)
    <<=	__ilshift__(self, other)
    &=	__iand__(self, other)
    |=	__ior__(self, other)
    ^=	__ixor__(self, other)

    unary operators :
    operator	magic method
    –	__neg__(self)
    +	__pos__(self)
    ~	__invert__(self)

    bracket:
    []  __getitem__(self, item)
    ()  __call__(self, *arg, **kwarg)
    """

    x, y = 0, 0
    z = 3

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """
        :param other:
        :return: self + other
        """
        return point(self.x + other.x, self.y + other.y)

    def __lt__(self, other):
        """

        :param other:
        :return: self < other
        """
        return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2

    def __iadd__(self, other):
        """

        :param other: other will be input as tuple like :
            if you use a += 1, 2, 3
            other will be (1, 2, 3)
            if you use a += 1
            other will be 1
        :return:
        """
        return self + other

    def __neg__(self):
        return point(-self.x, -self.y)

    def __getitem__(self, item):
        """

        :param item:
        :return: self[item]
        """
        if item == 0:
            return self.x
        if item == 1:
            return self.y

    def __call__(self, *args, **kwargs):
        return "args: " + str(args) + "\n\tkwargs: " + str( kwargs)


if __name__ == '__main__':

    p1 = point(1, 1)
    p2 = point(2, 2)
    print("p1 = point(1, 1)\n"
          "p2 = point(2, 2)\n"
          "---------\n"
          "p1 + p2\n-",
          p1 + p2,
          "\n---------")

    p1 += p2

    print("p1 += p2\np1\n-",
          p1,
          "\n---------")

    print("p1 < p2\n-",
          p1 < p2,
          "\n---------")

    print("-p1\n-",
          -p1[0],
          "\n---------")

    print("p1[0]\n-",
          p1[0],
          "\n---------")

    print("p1(1, 23,5 ,2, 43, a='a', c=lambda x:x)\n-",
          p1(1, 23,5 ,2, 43, a="a", c=lambda x:x),
          "\n---------")