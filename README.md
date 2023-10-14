
# 🌲 Tree Height Calculator 📏

In this tutorial, we will demonstrate how to calculate the height of a tree using the length of its shadow and the length of a stick and its shadow. The principle behind this is the similarity of triangles. 📐

## 📖 Introduction

When the sun casts shadows, the angles of elevation from the tips of the shadows to the top of the objects (stick and tree) are the same. By knowing the height of one object (the stick) and the lengths of the shadows, we can deduce the height of the second object (the tree). 🌳

## 📥 Getting User Input

First, we need to gather information from the user regarding:
- The length of the stick.
- The length of the stick's shadow.
- The length of the tree's shadow.

```python
stick_length = get_float_input("Enter the length of the stick (in meters): ")
stick_shadow_length = get_float_input("Enter the length of the stick's shadow (in meters): ")
tree_shadow_length = get_float_input("Enter the length of the tree's shadow (in meters): ")
```

## 📐 Calculating the Angle

Using the stick's height and shadow length, we'll calculate the angle of elevation between the stick and the ground.

```python
angle_radians = math.atan(stick_length / stick_shadow_length)
```

## 🌳 Calculating the Height of the Tree

We'll determine the height of the tree using the previously calculated angle and the length of the tree's shadow.

```python
tree_height = tree_shadow_length * math.tan(angle_radians)
```

## 🎨 Visualization

The program provides a simple ASCII representation of the tree, stick, and their shadows based on the entered values. Here's a sneak peek:

```
   ^
  ^^^
 ^^^^^
^^^^^^^
   |
```

## 🔄 Interactive Loop

Our enhanced version allows users to keep measuring multiple trees without restarting the program. After each measurement, users get to see the average height based on all the measurements they've taken! 📊

---

# 🚀 Getting Started

1. Clone this repository.
2. Run the `tree_height_calculator.py` script.
3. Follow the on-screen instructions to measure as many trees as you like!

---

Hope you find this tool helpful and fun! 🌍🌳
