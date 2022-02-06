class node_linked_list:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __len__(self):
        if self.value is None:
            return 0
        l = 1
        next = self.next
        while(next is not None):
            l += 1
            next = next.next
        return l

    def __copy__(self):
        return node_linked_list(self.value) if self.next is None else node_linked_list(self.value, self.next.__copy__())

class linked_list:
    first = None
    __len = 0

    def __init__(self, values=None):
        """

        :param values: a list of values
        """
        if values is None:
            values = []

        assert type(values) == type([]), "you should initialize with list"

        self.__len = len(values)

        if len(values) > 0:
            self.first = node_linked_list(values[0])

        node = self.first
        for i in range(1, len(values)):
            node.next = node_linked_list(values[i])
            node = node.next

    def is_empty(self):
        return self.__len == 0

    def append(self, value):
        """

        :param value: value to insert
        :return: append a node with (value = value, next = None) to the last node
        """
        self.__len += 1
        if self.first is None:
            self.first = node_linked_list(value)
        else:
            # find last node
            node = self.first
            while (node.next != None):
                node = node.next
            node.next = node_linked_list(value)

    def appends(self, values):
        """

        :param values: append many values
            values can be a list of values
                        or a linked_list
                        or a node
        :return:
        """
        if values is None:
            return
        if type(values) == type([]):
            # a list
            new = linked_list(values).first
            self.__len += len(values)
        elif type(values) == type(node_linked_list(0)):
            # a node
            new = values.__copy__()
            self.__len += len(values)
        elif type(values) == type(self):
            # a linked list
            if values.first is None:
                return
            new = values.first.__copy__()
            self.__len += len(values)
        else:
            assert False, (f"{type(values)} is not a valid type for appends() function")

        if self.first is None:
            self.first = new
        else:
            # find last node
            node = self.first
            while (node.next != None):
                node = node.next
            node.next = new

    def insert(self, index, value):
        """

        :param index: index of value after insert
        :param value: value to insert
        :return:
        """
        assert index >= 0, (f"index {index} should be >= 0")
        assert index <= self.__len, (f"index {index} should be <= length: {self.__len}")
        if index == 0:
            first = self.first
            self.first = node_linked_list(value, first)
            self.__len += 1
        else:
            node = self.first
            while(index != 1):
                node = node.next
                index -= 1
            next = node.next
            node.next = node_linked_list(value, next)
            self.__len += 1

    def remove(self, index):
        """
        :param index: index to be removed
        :return: the value removed
        """
        assert index >= 0, (f"index {index} should be >= 0")
        assert index < self.__len, (f"index {index} should be < length: {self.__len}")
        if index == 0:
            self.__len -= 1
            v = self.first.value
            self.first = self.first.next
            return v
        node = self.first
        while(index != 1):
            node = node.next
            index -= 1
        v = node.next.value
        node.next = node.next.next
        self.__len -= 1
        return v

    def __len__(self):
        return self.__len

    def __str__(self):
        s = []
        node = self.first
        while node is not None:
            s.append(node.value)
            node = node.next
        return str(s)

    def __getitem__(self, index):
        assert index >= 0, (f"index {index} should be >= 0")
        assert index < self.__len, (f"index {index} should be < length: {self.__len}")
        node = self.first
        while(index !=0):
            node = node.next
            index -= 1
        return node.value

    def __copy__(self):
        new = linked_list()
        new.__len = self.__len
        new.first = self.first.__copy__()
        return new


if __name__ == '__main__':

    a = linked_list()
    print("a = linked_list()\nprint(a, len(a))\n-", a, len(a), '\n----------')
    print("a.is_empty()\n-", a.is_empty(), '\n----------')

    a.append([1])

    print("a.append([1])\nprint(a)\n-", a, '\n----------')

    b = linked_list(["a", 1, 42, 12])
    print("b = linked_list(['a', 1, 42, 12])\nprint(b, len(b))\n-", b, len(b), '\n----------')

    b.appends([3, 4, 5, "a"])
    print("b.appends([3, 4, 5, 'a']) # append a list "
          "\nprint(b, len(b))\n-", b, len(b), '\n----------')

    c  = linked_list([8, 9, 0])
    a.appends(c)
    print(f"""c  = linked_list([8, 9, 0]) # append a linked list
a.appends(c)
print(a, len(a))
- {a} {len(a)}
----------""")

    b.appends(c.first)
    print(f"""b.appends(c.first) # append a node
print(b, len(b))
- {b} {len(b)}
----------""")

    a.insert(3, 1000)
    print("a.insert(3, 1000)\nprint(a)\n-", a, '\n----------')

    print("print(a.remove(0), a)\n-", a.remove(0), a, '\n----------')

    print("print(a[1])\n-", a[1], '\n----------')
