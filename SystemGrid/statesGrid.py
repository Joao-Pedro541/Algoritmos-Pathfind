from enum import Enum, auto

class BlockStates(Enum):
    START = auto()
    END = auto()

    EMPTY = auto()

    WALL = auto()

    OPEN = auto()
    CLOSED = auto()
    PATH = auto()

    CURRENT = auto()
    FRONTIER = auto()