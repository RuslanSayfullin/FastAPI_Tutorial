import typing

class DemoNTClass(typing.NamedTuple):
    """Класс, построенный с помощью typing.NamedTuple"""
    a: int           # <1>
    b: float = 1.1   # <2>
    c = 'spam'       # <3>
