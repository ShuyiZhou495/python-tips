from termcolor import colored

def kmp(t, pattern, v=True):
    pt = prefix_table(pattern)
    st = step_table(pattern, pt) # following the book
    if v:
        print_table("table", len(pattern), pattern=pattern, prefix=pt, skip=st)
        print_line("text", t)
        lines = 0

    i, j = 0, 0
    while i < len(t):
        if v:
            s = " " * i * 4 + seperate_string(pattern[:j])
        while (j < len(pattern) and i + j < len(t) and t[i + j] == pattern[j]):
            if v:
                s += seperate_string(pattern[j])
            j += 1
        if j == len(pattern):
            if v:
                print(f"{'found':10}|" + s + "<==")
            return i
        if v:
            print(f"skip ={st[j]:3} |" + s, end="")

        if i + j == len(t):
            if v:
                print()
            return False
        if v:
            print(colored(seperate_string(pattern[j]), 'red'), end="")
            print(seperate_string(pattern[j + 1:]))
            lines += 1
            if lines > 5:
                print_line("text", t)
                lines = 0
        i += st[j]
        j -= st[j]
        if j == -1:
            j += 1
    return False

def prefix_table(pattern):
    assert len(pattern) > 0, "why do you input an empty string?"
    res = [-1]
    for i in range(1, len(pattern)):
        res.append(find_prefix(pattern[:i]))
    return res

def find_prefix(s):
    for i in range(len(s) - 1, 0, -1):
        if s[:i] == s[-i:]:
            return i
    return 0

def step_table(pattern, prefix):
    res = [1]
    for i, p in enumerate(prefix[1:], start=1):
        res.append(i - p if pattern[p] != pattern[i] else i - p + res[p])
    return res

def seperate_string(s, delimeter="", size=4):
    """
    you can understand as print f"s[i]:4"
    :param s:
    :param delimeter:
    :param size:
    :return:
    """
    res = ""
    for c in s:
        length = len(str(c))
        l = (size - length) // 2
        r = size - l - length - len(delimeter)
        res += " " * l + str(c) + " " * r + delimeter
    return res


def print_line(comment, content):
    print(f"{comment:10}", end="|")
    print(seperate_string(content, delimeter="|"))

def print_table(title, length, **kwargs):
    """

    :param title: title of table
    :param length: length of data to be input
    :param kwargs: name and value of data
    :return:
    """
    print("=" * 4 + f" {title} " + "=" * (length * 4 + 5 - len(title)))
    print_line("index", range(length))
    for k, v in kwargs.items():
        print_line(k, v)
    print("=" * (length * 4 + 11))
