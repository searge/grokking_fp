class TipCalculator:
    def __init__(self) -> None:
        self.names: list[str] = []
        self.tip_percentage: int = 0

    def add_person(self, name: str) -> None:
        self.names.append(name)
        if len(self.names) > 5:
            self.tip_percentage = 20
        else:
            self.tip_percentage = 10

    def get_names(self) -> list[str]:
        return self.names

    def get_tip_percentage(self) -> int:
        return self.tip_percentage

if __name__ == "__main__":
    tip_calculator = TipCalculator()
    visitors: list[str] = ["John", "Jane", "Joe", "Jill", "Jack", "Joel"]
    for visitor in visitors:
        tip_calculator.add_person(visitor)
    print(tip_calculator.get_names())
    print(tip_calculator.get_tip_percentage())
