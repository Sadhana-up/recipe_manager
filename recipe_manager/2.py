##ALL CODE IN CASE U WANT THAT

# class Ingredient:
#     def __init__(self, quantity, name, unit):
#         self.quantity = quantity
#         self.name = name
#         self.unit = unit

#     def __str__(self):
#         return f"{self.quantity} {self.unit} of {self.name}"

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, new_name):
#         if not isinstance(new_name, str) or new_name.strip() == "": --> empty cha ya invalid cha vanera check garne huhu
#             raise ValueError("Ingredient name must be a non-empty string.")
#         self._name = new_name


# class Category:
#     def __init__(self, name, description):
#         self._name = name
#         self.description = description

#     @property
#     def name(self):
#         return self._name

#     def __str__(self):
#         return f"Category: {self.name} — {self.description}"


# class Recipe:
#     def __init__(self, name, category, prep_time, cook_time):
#         self.name = name
#         self.category = category
#         self.prep_time = prep_time
#         self.cook_time = cook_time
#         self.ingredients = []
#         self.instructions = []

#     def add_ingredient(self, ingredient):
#         self.ingredients.append(ingredient)

#     def remove_ingredient(self, ingredient_name):
#         for ing in self.ingredients:
#             if ing.name.lower() == ingredient_name.lower():
#                 self.ingredients.remove(ing)
#                 break

#     def add_instruction(self, step):
#         self.instructions.append(step)

#     def display_recipe(self):
#         print(f"\nRecipe: {self.name}")
#         print(f"{self.category}")
#         print(f"Prep Time: {self.prep_time} mins | Cook Time: {self.cook_time} mins\n")
#         print("Ingredients:")
#         for ing in self.ingredients:
#             print(f" - {ing}")
#         print("\nInstructions:")
#         for i, step in enumerate(self.instructions, 1):
#             print(f"{i}. {step}")

# # dessert = Category("Dessert", "Sweet dishes after meals")
# # cake = Recipe("Chocolate Cake", dessert, 20, 30)

# # cake.add_ingredient(Ingredient(200, "Flour", "grams"))
# # cake.add_ingredient(Ingredient(100, "Sugar", "grams"))
# # cake.add_instruction("Mix all ingredients.")

# # cake.display_recipe()


# class RecipeManager:
#     def __init__(self):
#         self.recipes = []
#         self.categories = []

#     def add_category(self, category):
#         if category not in self.categories:
#             self.categories.append(category)

#     def add_recipe(self, recipe):
#         self.recipes.append(recipe)
#         if recipe.category not in self.categories:
#             self.categories.append(recipe.category)

#     def remove_recipe(self, recipe_name):
#         for recipe in self.recipes:
#             if recipe.name.lower() == recipe_name.lower():
#                 self.recipes.remove(recipe)
#                 break

#     def get_recipe_by_name(self, recipe_name):
#         for recipe in self.recipes:
#             if recipe.name.lower() == recipe_name.lower():
#                 return recipe
#         return None

#     def get_recipes_by_category(self, category_name):
#         return [r for r in self.recipes if r.category.name.lower() == category_name.lower()]

#     def list_all_recipes(self):
#         if not self.recipes:
#             print("No recipes available.")
#             return
#         print("\nAll Recipes:")
#         for r in self.recipes:
#             print(f" - {r.name} ({r.category.name})")

#     def list_categories(self):
#         if not self.categories:
#             print("No categories added yet.")
#             return
#         print("\nAvailable Categories:")
#         for c in self.categories:
#             print(f" - {c.name}")
