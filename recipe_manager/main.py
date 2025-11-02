from recipe_manager import Ingredient, Category, Recipe, RecipeManager

if __name__ == "__main__":
    dessert = Category("Dessert", "Sweet dishes after meals")
    cake = Recipe("Chocolate Cake", dessert, 20, 30)

    cake.add_ingredient(Ingredient(200, "Flour", "grams"))
    cake.add_ingredient(Ingredient(100, "Sugar", "grams"))
    cake.add_instruction("Mix all ingredients.")
    cake.add_instruction("Bake at 180°C for 30 minutes.")

    manager = RecipeManager()
    manager.add_recipe(cake)

    manager.list_all_recipes()
    recipe = manager.get_recipe_by_name("Chocolate Cake")
    if recipe:
        recipe.display_recipe()
