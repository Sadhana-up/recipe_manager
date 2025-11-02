class RecipeManager:
    def __init__(self):
        self.recipes = []
        self.categories = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        if recipe.category not in self.categories:
            self.categories.append(recipe.category)

    def remove_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                self.recipes.remove(recipe)
                break

    def get_recipe_by_name(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                return recipe
        return None

    def get_recipes_by_category(self, category_name):
        return [r for r in self.recipes if r.category.name.lower() == category_name.lower()]

    def list_all_recipes(self):
        if not self.recipes:
            print("No recipes available.")
            return
        print("\nAll Recipes:")
        for r in self.recipes:
            print(f" - {r.name} ({r.category.name})")

    def list_categories(self):
        if not self.categories:
            print("No categories added yet.")
            return
        print("\nAvailable Categories:")
        for c in self.categories:
            print(f" - {c.name}")
