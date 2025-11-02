class Recipe:
    def __init__(self, name, category, prep_time, cook_time):
        self.name = name
        self.category = category
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.ingredients = []
        self.instructions = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient_name):
        for ing in self.ingredients:
            if ing.name.lower() == ingredient_name.lower():
                self.ingredients.remove(ing)
                break

    def add_instruction(self, step):
        self.instructions.append(step)

    def display_recipe(self):
        print(f"\nRecipe: {self.name}")
        print(f"{self.category}")
        print(f"Prep Time: {self.prep_time} mins | Cook Time: {self.cook_time} mins\n")
        print("Ingredients:")
        for ing in self.ingredients:
            print(f" - {ing}")
        print("\nInstructions:")
        for i, step in enumerate(self.instructions, 1):
            print(f"{i}. {step}")
