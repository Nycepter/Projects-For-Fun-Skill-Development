import random
import pickle

# Load existing data or initialize empty lists
try:
    with open('themes.pkl', 'rb') as file:
        themes = pickle.load(file)
except FileNotFoundError:
    themes = []

try:
    with open('types.pkl', 'rb') as file:
        types = pickle.load(file)
except FileNotFoundError:
    types = []


def save_input():
    # Allow multiple entries for themes in comma-separated format
    theme_input = input("Enter themes (comma-separated): ")
    theme_inputs = [t.strip() for t in theme_input.split(',')]
    themes.extend(theme_inputs)

    # Allow multiple entries for types in comma-separated format
    type_input = input("Enter types (comma-separated): ")
    type_inputs = [t.strip() for t in type_input.split(',')]
    types.extend(type_inputs)

    # Save updated lists to files using pickle
    with open('themes.pkl', 'wb') as file:
        pickle.dump(themes, file)

    with open('types.pkl', 'wb') as file:
        pickle.dump(types, file)


def pick_and_output():
    if not themes:
        print("Themes list is empty. Please add themes.")
        return

    if not types:
        print("Types list is empty. Please add types.")
        return

    # Randomly pick 1 item from themes list
    selected_theme = random.choice(themes)
    print("Selected theme:", selected_theme)

    # Allow multiple selections for types
    num_selected_types = min(3, len(types))
    selected_types = random.sample(types, num_selected_types)
    print("Selected types:", selected_types)

    # Remove the selected theme from the themes list
    themes.remove(selected_theme)

    # Save updated lists to files using pickle
    with open('themes.pkl', 'wb') as file:
        pickle.dump(themes, file)


# Main program loop
while True:
    print("\n1. Add Theme and/or Types")
    print("2. Pick Theme and Types")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        save_input()
    elif choice == '2':
        pick_and_output()
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
