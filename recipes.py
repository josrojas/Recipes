

def main():
  
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