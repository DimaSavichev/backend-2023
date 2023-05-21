def operation(a: int, b: int) -> int | None:
    if (a is None) or (b is None):
        return None
    return a + b
