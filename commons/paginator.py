from typing import TypedDict

class PaginationData(TypedDict):
    count: int
    pages: int
    next: bool
    previous: bool