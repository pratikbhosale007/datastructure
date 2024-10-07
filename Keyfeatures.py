## Key Features of Lists in Python

#Lists are one of the most versatile data structures in Python. They are ordered collections of items, which can be of any data type. Here are some of their key features:

### 1. **Ordered Sequence:**
#* **Indexing:** Elements in a list are accessed by their index, starting from 0.
#* **Slicing:** You can extract sublists using slicing, similar to strings.

### 2. **Mutable:**
#* **Modification:** Elements in a list can be changed, added, or removed after creation.
#* **Dynamic Size:** Lists can grow or shrink as needed.

### 3. **Heterogeneous Elements:**
#* **Mixed Data Types:** Lists can contain elements of different data types (e.g., integers, strings, floats, even other lists).

### 4. **Methods:**
#* **Built-in Functions:** Lists have many built-in methods that provide various operations, such as:
   # * **`append()`:** Adds an element to the end of the list.
    #* **`insert()`:** Inserts an element at a specified index.
    # **`remove()`:** Removes the first occurrence of a specified element.
    #* **`pop()`:** Removes an element at a specified index or the last element (if no index is provided).
    #* **`extend()`:** Appends another list to the end of the current list.
    #* **`index()`:** Returns the index of the first occurrence of a specified element.
    #* **`count()`:** Returns the number of occurrences of a specified element.
    #* **`sort()`:** Sorts the elements of the list in ascending order.
    #* **`reverse()`:** Reverses the order of the elements in the list.
    #* **`copy()`:** Creates a shallow copy of the list.

### 5. **Nested Lists:**
#* **Multi-dimensional Structures:** Lists can contain other lists, creating nested structures.

### Example:

my_list = [1, "hello", 3.14, [True, False]]

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: [True, False]

# Modifying elements
my_list[1] = "world"
print(my_list)  # Output: [1, 'world', 3.14, [True, False]]

# Adding elements
my_list.append(5)
print(my_list)  # Output: [1, 'world', 3.14, [True, False], 5]

# Removing elements
my_list.remove(3.14)
print(my_list)  # Output: [1, 'world', [True, False], 5]