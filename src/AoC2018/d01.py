def run_1(inp):
    """
    >>> t = "\\n".join('+1, +1, +1'.split(','))
    >>> run_1(t)
    3
    >>> t = "\\n".join('+1, +1, -2'.split(','))
    >>> run_1(t)
    0
    >>> t = "\\n".join('-1, -2, -3'.split(','))
    >>> run_1(t)
    -6
    """
    res = 0

    shifts = inp.splitlines()

    for f in shifts:
        res += int(f)

    return res


def run_2(inp):
    """
    >>> t = "\\n".join('-1, +1'.split(','))
    >>> run_2(t)
    0
    >>> t = "\\n".join('+3, +3, +4, -2, -4'.split(','))
    >>> run_2(t)
    10
    >>> t = "\\n".join('-6, +3, +8, +5, -6'.split(','))
    >>> run_2(t)
    5
    >>> t = "\\n".join('+7, +7, -2, -7, -4'.split(','))
    >>> run_2(t)
    14
    """
    shifts = inp.splitlines()

    freqs = set()
    freqs.add(0)
    f = 0

    while True:
        for s in shifts:
            f += int(s)
            if f in freqs:
                return f
            else:
                freqs.add(f)
