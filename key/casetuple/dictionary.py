## Adding, Modifying, and Deleting Items in a Dictionary

#**Dictionaries** in Python are unordered collections of key-value pairs. Each key must be unique, and the values can be of any data type.

### Adding Items
#* **Direct Assignment:** Assign a value to a new key. If the key already exists, the value will be updated.

my_dict = {'name': 'Alice', 'age': 30}
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


### Modifying Items
#* **Direct Assignment:** Assign a new value to an existing key.

my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

### Deleting Items
#* **`del` Keyword:** Use the `del` keyword with the key to delete the corresponding key-value pair.
#* **`pop()` Method:** Removes and returns the value associated with the specified key. If the key doesn't exist, it raises a `KeyError`.
#* **`popitem()` Method:** Removes and returns an arbitrary key-value pair from the dictionary.


del my_dict['city']
print(my_dict)  # Output: {'name': 'Alice', 'age': 31}

value = my_dict.pop('age')
print(my_dict)  # Output: {'name': 'Alice'}
print(value)  # Output: 31

key, value = my_dict.popitem()
print(my_dict)  # Output: {}
print(key, value)  # Output: name Alice


#**Additional Notes:**

#* Dictionaries are mutable, so you can change their contents after creation.
#* Keys in a dictionary must be immutable data types (e.g., strings, numbers, tuples).
#* The order of elements in a dictionary is not guaranteed.
#* You can use the `clear()` method to remove all items from a dictionary.