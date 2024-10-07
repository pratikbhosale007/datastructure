## Key Features of Sets in Python

#Sets are unordered collections of unique elements in Python. They are similar to lists and tuples, but with the following key differences:

#1. **Unordered:** Elements in a set do not have a specific order.
#2. **Unique Elements:** Sets cannot contain duplicate elements.
#3. **Immutable Elements:** Elements within a set must be immutable (e.g., numbers, strings, tuples, but not lists or dictionaries).
#4. **Set Operations:** Sets support various mathematical set operations, such as union, intersection, difference, and symmetric difference.

## Examples of Set Use

### Creating Sets:

my_set = {1, 2, 3, 4}
empty_set = set()  # Create an empty set


### Adding and Removing Elements:

my_set.add(5)  # Add an element
my_set.remove(3)  # Remove an element
my_set.discard(6)  # Remove an element if it exists (no error if not found)


### Set Operations:

set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Union: Combine elements from both sets
union_set = set1 | set2  # Or set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4}

# Intersection: Find elements common to both sets
intersection_set = set1 & set2  # Or set1.intersection(set2)
print(intersection_set)  # Output: {2, 3}

# Difference: Find elements in set1 but not in set2
difference_set = set1 - set2  # Or set1.difference(set2)
print(difference_set)  # Output: {1}

# Symmetric Difference: Find elements in either set but not both
symmetric_difference_set = set1 ^ set2  # Or set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 4}


### Membership Testing:

if 2 in my_set:
    print("2 is in the set")


### Common Use Cases:
#* **Removing duplicates:** Sets can be used to efficiently remove duplicates from a list or tuple.
#* **Membership testing:** Quickly check if an element exists in a set.
#* **Set operations:** Perform mathematical operations on sets, such as finding unions, intersections, differences, and symmetric differences.
#* **Data analysis:** Sets can be used for data analysis tasks, such as finding common elements or unique values.x