"""Shopping cart implementation with discount functionality.

This module contains a ShoppingCart class that manages items and applies
discounts based on the presence of specific items (books).
"""


class ShoppingCartBad:
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
            A copy of the list of all items currently in the cart.
        """
        return self.items.copy()

    def remove_item(self, item: str) -> None:
        """Remove an item from the shopping cart.

        Args:
            item: The name of the item to remove from the cart.
        """
        self.items.remove(item)
        if item == "Book":
            self.book_added = False


class ShoppingCartRecalculating:
    """A shopping cart that recalculates discount based on current items.

    Unlike ShoppingCartBad, this implementation calculates the discount by
    checking if a book is currently in the cart, rather than tracking
    whether a book was ever added.
    """

    def __init__(self) -> None:
        """Initialize an empty shopping cart."""
        self.items: list[str] = []

    def add_item(self, item: str) -> None:
        """Add an item to the shopping cart.

        Args:
            item: The name of the item to add to the cart.
        """
        self.items.append(item)

    def get_items(self) -> list[str]:
        """Get all items in the shopping cart.

        Returns
        -------
            A copy of the list of all items currently in the cart.
        """
        return self.items.copy()

    def get_discount_percentage(self) -> int:
        """Get the discount percentage for the current cart.

        Returns
        -------
            5 if a book is currently in the cart, 0 otherwise.
        """
        if "Book" in self.items:
            return 5
        return 0

    def remove_item(self, item: str) -> None:
        """Remove an item from the shopping cart.

        Args:
            item: The name of the item to remove from the cart.
        """
        self.items.remove(item)


class ShoppingCartStatic:
    """Shopping cart with static methods - functional approach."""

    @staticmethod
    def get_discount_percentage(items: list[str]) -> int:
        """Calculate discount percentage based on items list.

        Args:
            items: List of items in the shopping cart.

        Returns
        -------
            5 if the list contains a book, 0 otherwise.
        """
        if "Book" in items:
            return 5
        return 0


if __name__ == "__main__":
    cart = ShoppingCartBad()
    cart.add_item("Shirt")
    cart.add_item("Book")
    cart.add_item("Shoes")

    # It supposed to remove "Book" from the cart
    # But we are using copy of the list, so it will not be removed
    # from the original list
    cart.get_items().remove("Book")
    # Test removing "Book" from the cart
    cart.remove_item("Book")
    # We will get a problem, when the list get more Books

    print("Items in cart:", cart.get_items())
    print("Discount percentage:", cart.get_discount_percentage())

    # SOLUTION 2: RECALCULATING
    cart2 = ShoppingCartRecalculating()
    cart2.add_item("Book")
    cart2.add_item("Book") # adding a second book
    try:
        assert cart2.get_discount_percentage() == 5
        print("Assertion passed")
    except AssertionError:
        print("Assertion failed")
    cart2.add_item("Shoes")
    cart2.remove_item("Book")

    try:
        assert cart2.get_items() == ["Book", "Shoes"]
        print("Assertion passed")
    except AssertionError:
        print("Assertion failed")
    try:
        assert cart2.get_discount_percentage() == 5
        print("Assertion passed")
    except AssertionError:
        print("Assertion failed")

    print("Items in cart:", cart2.get_items())
    print("Discount percentage:", cart2.get_discount_percentage())

    # SOLUTION 3: JUST A FUNCTION
    just_apple: list[str] = ["Apple"]
    print(ShoppingCartStatic.get_discount_percentage(just_apple))
    apple_and_book: list[str] = ["Apple", "Book"]
    print(ShoppingCartStatic.get_discount_percentage(apple_and_book))
    try:
        assert ShoppingCartStatic.get_discount_percentage(just_apple) == 0
        assert ShoppingCartStatic.get_discount_percentage(apple_and_book) == 5
        print("Assertion passed")
    except AssertionError:
        print("Assertion failed")
    # Imperative usage
    items: list[str] = []
    try:
        assert ShoppingCartStatic.get_discount_percentage(items) == 0
        print("Assertion of empty list passed")
    except AssertionError:
        print("Assertion of empty list failed")
    items.append("Apple")
    try:
        assert ShoppingCartStatic.get_discount_percentage(items) == 0
        print("Assertion of list with one item passed")
    except AssertionError:
        print("Assertion of list with one item failed")
    items.append("Book")
    try:
        assert ShoppingCartStatic.get_discount_percentage(items) == 5
        print("Assertion of list with two items with book passed")
    except AssertionError:
        print("Assertion of list with two items failed")
