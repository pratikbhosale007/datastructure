## Accessing, Modifying, and Deleting Elements in a List

### Accessing Elements
#* **Indexing:** Use square brackets `[]` to access elements by their index. The first element has an index of 0.
#* **Negative Indexing:** Access elements from the end of the list using negative indices. For example, `-1` refers to the last element.

#**Example:**

my_list = [10, 20, 30, 40, 50]

# Access the first element
print(my_list[0])  # Output: 10

# Access the last element
print(my_list[-1])  # Output: 50

# Access the element at index 2
print(my_list[2])  # Output: 30


### Modifying Elements
#* **Direct Assignment:** Assign a new value to an element using its index.

#**Example:**

my_list = [10, 20, 30, 40, 50]

# Change the value at index 2 to 100
my_list[2] = 100
print(my_list)  # Output: [10, 20, 100, 40, 50]

### Deleting Elements
#* **`del` Keyword:** Use the `del` keyword with the index of the element to delete it.
# **`pop()` Method:** Removes an element at a specified index or the last element if no index is provided. Returns the removed element.
#* **`remove()` Method:** Removes the first occurrence of a specified value.

#**Example:**

my_list = [10, 20, 30, 40, 50]

# Delete the element at index 1 using `del`
del my_list[1]
print(my_list)  # Output: [10, 30, 40, 50]

# Remove the last element using `pop()`
removed_element = my_list.pop()
print(my_list)  # Output: [10, 30, 40]
print(removed_element)  # Output: 50

# Remove the first occurrence of 30 using `remove()`
my_list.remove(30)
print(my_list)  # Output: [10, 40]