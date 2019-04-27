def FabioncciRecursion(n):
    if n<2:
        return n

    return FabioncciRecursion(n-1)+FabioncciRecursion(n-2)

FabioncciRecursion(6)

