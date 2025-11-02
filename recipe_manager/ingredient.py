class Ingredient:
    def __init__(self, quantity, name, unit):
        self.quantity = quantity
        self.name = name
        self.unit = unit

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or new_name.strip() == "":
            raise ValueError("Ingredient name must be a non-empty string.")
        self._name = new_name
