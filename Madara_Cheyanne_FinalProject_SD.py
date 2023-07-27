import tkinter as tk
from tkinter import ttk, messagebox

# This function creates a new window to add a recipe
def add_recipe():
    add_recipe_window = tk.Toplevel(root)
    add_recipe_window.title('Add Recipe Window')

    ttk.Label(add_recipe_window, text="Recipe Name").grid(row=0, pady=10)
    ttk.Label(add_recipe_window, text="Ingredients").grid(row=1, pady=10)
    ttk.Label(add_recipe_window, text="Instructions").grid(row=2, pady=10)

    name_entry = ttk.Entry(add_recipe_window)
    ingredients_entry = ttk.Entry(add_recipe_window)
    instructions_entry = ttk.Entry(add_recipe_window)

    name_entry.grid(row=0, column=1, pady=10)
    ingredients_entry.grid(row=1, column=1, pady=10)
    instructions_entry.grid(row=2, column=1, pady=10)

    def save_recipe():
        name = name_entry.get()
        ingredients = ingredients_entry.get()
        instructions = instructions_entry.get()

        if not name or not ingredients or not instructions:
            messagebox.showerror("Invalid Input", "All fields are required!")
            return

        recipes[name] = {'ingredients': ingredients, 'instructions': instructions}
        messagebox.showinfo("Success", "Recipe has been saved successfully!")

    ttk.Button(add_recipe_window, text="Save Recipe", command=save_recipe).grid(row=3, column=1, pady=10)

# This function creates a new window to view a recipe
def open_recipe():
    recipe_name = name_entry.get()

    if not recipe_name:
        messagebox.showerror("Invalid Input", "Please enter a recipe name!")
        return

    recipe = recipes.get(recipe_name)

    if not recipe:
        messagebox.showerror("Not Found", "Recipe not found!")
        return

    recipe_window = tk.Toplevel(root)
    recipe_window.title('Recipe Window')

    ttk.Label(recipe_window, text="Recipe Name: " + recipe_name).pack(pady=10)
    ttk.Label(recipe_window, text="Ingredients: " + recipe['ingredients']).pack(pady=10)
    ttk.Label(recipe_window, text="Instructions: " + recipe['instructions']).pack(pady=10)

# Main window
root = tk.Tk()
root.title('Recipe Keeper')

recipes = {}

ttk.Label(root, text="Enter recipe name:").pack(pady=10)

name_entry = ttk.Entry(root)
name_entry.pack(pady=10)

ttk.Button(root, text="Add Recipe", command=add_recipe).pack(pady=10)
ttk.Button(root, text="Open Recipe", command=open_recipe).pack(pady=10)
ttk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

root.mainloop()
