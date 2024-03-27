import json

class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def display_recipe(self):
        print(f"Recipe: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient.name}: {ingredient.quantity}")

    def edit_recipe(self):
        new_name = input("Enter the new name for the recipe: ")
        self.name = new_name

    def edit_ingredient(self, ingredient_name):
        for ingredient in self.ingredients:
            if ingredient.name == ingredient_name:
                new_name = input("Enter the new name for the ingredient: ")
                new_quantity = input("Enter the new quantity for the ingredient: ")
                ingredient.name = new_name
                ingredient.quantity = new_quantity
                print("Ingredient edited successfully!")
                return
        print("Ingredient not found!")

    def to_dict(self):
        return {"name": self.name, "ingredients": [{"name": i.name, "quantity": i.quantity} for i in self.ingredients]}

def save_recipes(recipes):
    with open('data.json', 'w') as f:
        json.dump([r.to_dict() for r in recipes], f)

def load_recipes():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        return [Recipe(d['name'], [Ingredient(i['name'], i['quantity']) for i in d['ingredients']]) for d in data]
    except FileNotFoundError:
        return []

def main():
    recipes = load_recipes() # Load recipes from file

    while True:
        print("1. Add recipe")
        print("2. Add ingredient to recipe")
        print("3. Display recipe details")
        print("4. Edit recipe")
        print("5. Edit ingredient")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            recipe_name = input("Enter recipe name: ")
            recipe = Recipe(recipe_name, [])
            recipes.append(recipe)
            save_recipes(recipes)
            print("Recipe added successfully!")

        elif choice == "2":
            recipe_name = input("Enter recipe name: ")
            ingredient_name = input("Enter ingredient name: ")
            ingredient_quantity = input("Enter ingredient quantity: ")

            for recipe in recipes:
                if recipe.name == recipe_name:
                    ingredient = Ingredient(ingredient_name, ingredient_quantity)
                    recipe.add_ingredient(ingredient)
                    save_recipes(recipes)
                    print("Ingredient added successfully!")
                    break
            else:
                print("Recipe not found!")

        elif choice == "3":
            recipe_name = input("Enter recipe name: ")

            for recipe in recipes:
                if recipe.name == recipe_name:
                    recipe.display_recipe()
                    break
            else:
                print("Recipe not found!")

        elif choice == "4":
            recipe_name = input("Enter recipe name: ")

            for recipe in recipes:
                if recipe.name == recipe_name:
                    recipe.edit_recipe()
                    save_recipes(recipes)
                    print("Recipe edited successfully!")
                    break
            else:
                print("Recipe not found!")

        elif choice == "5":
            recipe_name = input("Enter recipe name: ")
            ingredient_name = input("Enter the name of the ingredient to edit: ")

            for recipe in recipes:
                if recipe.name == recipe_name:
                    recipe.edit_ingredient(ingredient_name)
                    save_recipes(recipes)
                    break
            else:
                print("Recipe not found!")

        elif choice == "6":
            print("Thanks for using the app!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()