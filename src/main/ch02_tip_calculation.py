"""Tip calculation examples demonstrating imperative vs functional styles."""


class TipCalculator:
    """A tip calculator that adjusts tip percentage based on group size.

    Uses imperative style with mutable state. Tip percentage is 20% for groups
    larger than 5 people, otherwise 10%.
    """

    def __init__(self) -> None:
        self.names: list[str] = []
        self.tip_percentage: int = 0

    def add_person(self, name: str) -> None:
        """Add a person to the group and update tip percentage.

        Parameters
        ----------
        name : str
            The name of the person to add to the group.
        """
        self.names.append(name)
        if len(self.names) > 5:
            self.tip_percentage = 20
        else:
            self.tip_percentage = 10

    def get_names(self) -> list[str]:
        """Get the list of names in the group.

        Returns
        -------
        list[str]
            The list of names currently in the group.
        """
        return self.names

    def get_tip_percentage(self) -> int:
        """Get the current tip percentage based on group size.

        Returns
        -------
        int
            The tip percentage (10% or 20%) based on current group size.
        """
        return self.tip_percentage


class TipCalculatorStatic:
    """A tip calculator using functional style with static methods.

    Provides pure functions without mutable state. Tip percentage is 20%
    for groups larger than 5 people, otherwise 10%.
    """

    @staticmethod
    def get_tip_percentage(names: list[str]) -> int:
        """Calculate tip percentage based on group size (pure function).

        Parameters
        ----------
        names : list[str]
            The list of names in the group.

        Returns
        -------
        int
            The tip percentage (10% or 20%) based on group size.
        """
        if len(names) > 5:
            return 20
        return 10


if __name__ == "__main__":
    tip_calculator = TipCalculator()
    visitors: list[str] = ["John", "Jane", "Joe", "Jill", "Jack", "Joel"]
    for visitor in visitors:
        tip_calculator.add_person(visitor)
    print(tip_calculator.get_names())
    print("Imperative style: Instance method")
    print(tip_calculator.get_tip_percentage())

    # Functional style
    print("Functional style: Static method")
    tip_calculator2 = TipCalculatorStatic()
    print(tip_calculator2.get_tip_percentage(visitors))
