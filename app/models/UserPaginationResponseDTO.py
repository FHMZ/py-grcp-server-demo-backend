from typing import List, Generic, TypeVar

T = TypeVar('T')

class UserPaginationResponseDTO(Generic[T]):
    def __init__(self, items: List[T], page: int, page_size: int, total_items: int):
        self.items = items
        self.page = page
        self.page_size = page_size
        self.total_items = total_items

    def to_dict(self) -> dict:
        """Converts the pagination object to a dictionary."""
        return {
            "items": [item.to_dict() for item in self.items],
            "page": self.page,
            "page_size": self.page_size,
            "total_items": self.total_items
        }
