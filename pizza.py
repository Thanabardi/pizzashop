from enum import Enum


class PizzaSize(Enum):
    small = 120
    medium = 200
    large = 280
    jumbo = 400

    @property
    def price(self):
        return self.value

    def __str__(self):
        return self.name


class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size: PizzaSize):
        if not isinstance(size, PizzaSize):
            raise TypeError("size must be a pizza size")
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        return self.size.value + 20 * len(self.toppings)

    def add_topping(self, topping):
        """Add a topping to the pizza."""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def __str__(self):
        """
        Create printable description of the pizza.

        such as "small pizza with muschroom" or "small plain pizza"
        """
        description = self.size.name
        if self.toppings:
            description += " pizza with " + ", ".join(self.toppings)
        else:
            description += " plain cheeze pizza"
        return description
