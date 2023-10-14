
import math

def calculate_tree_height():
    # Getting User Input
    stick_length = float(input("Enter the length of the stick (in meters): "))
    stick_shadow_length = float(input("Enter the length of the stick's shadow (in meters): "))
    tree_shadow_length = float(input("Enter the length of the tree's shadow (in meters): "))

    # Calculating the Angle
    angle_radians = math.atan(stick_length / stick_shadow_length)

    # Calculating the Height of the Tree
    tree_height = tree_shadow_length * math.tan(angle_radians)

    # Output
    print(f"The height of the tree is {tree_height:.2f} meters.")

if __name__ == "__main__":
    calculate_tree_height()
