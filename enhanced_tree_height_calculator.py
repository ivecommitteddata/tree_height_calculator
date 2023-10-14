import math

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calculate_tree_height():
    # Getting User Input
    stick_length = get_float_input("Enter the length of the stick (in meters): ")
    stick_shadow_length = get_float_input("Enter the length of the stick's shadow (in meters): ")
    tree_shadow_length = get_float_input("Enter the length of the tree's shadow (in meters): ")

    # Calculating the Angle
    angle_radians = math.atan(stick_length / stick_shadow_length)

    # Calculating the Height of the Tree
    tree_height = tree_shadow_length * math.tan(angle_radians)
    
    return tree_height

def display_ascii_tree(tree_height):
    tree_representation = """
       ^
      ^^^
     ^^^^^
    ^^^^^^^
       |
    """
    print(tree_representation)
    print(f"The height of the tree is {tree_height:.2f} meters.")

def main():
    tree_heights = []
    while True:
        tree_height = calculate_tree_height()
        tree_heights.append(tree_height)
        display_ascii_tree(tree_height)
        
        avg_height = sum(tree_heights) / len(tree_heights)
        print(f"Average tree height (from {len(tree_heights)} measurements): {avg_height:.2f} meters.")
        
        cont = input("Do you want to measure another tree? (yes/no) ").lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()
