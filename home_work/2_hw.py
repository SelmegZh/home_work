def task_1():
    a: int = 5
    print(a, 'относится к типу ', type(a))
    b: float = 4.89
    print(b, 'относится к типу ', type(b))
    c: str = 'str'
    print(c, 'относится к типу ', type(c))
    d: list = [1, 2, 3]
    print(d, 'относится к типу ', type(d))
    e: bool = True
    print(e, 'относится к типу ', type(e))
    return (a, b, c, d, e)
print(task_1())
def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0], a[1], a[2])
    return a
print(task_2())
def task_3() -> int:
    b: int = 5
    return b ** 2
print(task_3())
