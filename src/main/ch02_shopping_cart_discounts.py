"""Shopping cart implementation with discount functionality.

This module contains a ShoppingCart class that manages items and applies
discounts based on the presence of specific items (books).
"""


class ShoppingCart:
    """A shopping cart that tracks items and provides discount functionality.

    The cart applies a 5% discount when a book is added to the cart.
    """

    def __init__(self) -> None:
        """Initialize an empty shopping cart."""
        self.items: list[str] = []
        self.book_added: bool = False

    def add_item(self, item: str) -> None:
        """Add an item to the shopping cart.

        Args:
            item: The name of the item to add to the cart.
        """
        self.items.append(item)
        if item == "Book":
            self.book_added = True

    def get_discount_percentage(self) -> int:
        """Get the discount percentage for the current cart.

        Returns
        -------
            5 if a book has been added to the cart, 0 otherwise.
        """
        if self.book_added:
            return 5
        return 0

    def get_items(self) -> list[str]:
        """Get all items in the shopping cart.

        Returns
        -------
            A list of all items currently in the cart.
        """
        return self.items.copy()


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Shirt")
    cart.add_item("Book")
    cart.add_item("Shoes")

    print("Items in cart:", cart.get_items())
    print("Discount percentage:", cart.get_discount_percentage())
