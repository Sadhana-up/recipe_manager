class Category:
    def __init__(self, name, description):
        self._name = name
        self.description = description

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Category: {self.name} — {self.description}"
