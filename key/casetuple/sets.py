## Use Cases of Tuples and Sets in Python

#**Tuples** and **sets** are both data structures in Python, but they have distinct characteristics and use cases.

### Tuples

#Tuples are **immutable** ordered collections of elements. They are often used in scenarios where:

#* **Data needs to be protected from accidental modification:** Tuples provide a way to ensure that data remains unchanged throughout a program's execution.
#e* **Values are returned from functions:** Tuples can be used to return multiple values from a function.
#* **Data needs to be used as keys in dictionaries:** Tuples can be used as keys in dictionaries because they are immutable.

#**Examples:**

#* **Returning multiple values from a function:**
def calculate_area(length, width):
      return (length * width, 2 * (length + width))

area, perimeter = calculate_area(5, 3)
print(area, perimeter)  # Output: 15 16

#* **Using tuples as dictionary keys:**

person = {
      ('John', 'Doe'): 30,
      ('Jane', 'Smith'): 25
  }
print(person[('John', 'Doe')])  # Output: 30

### Sets

#Sets are **unordered** collections of **unique** elements. They are often used in scenarios where:

#* **Duplicate values need to be removed:** Sets can efficiently remove duplicates from a collection.
#* **Membership testing needs to be performed efficiently:** Checking if an element exists in a set is faster than in a list.
#* **Set operations need to be performed:** Sets support operations like union, intersection, difference, and symmetric difference.

#**Examples:**

#* **Removing duplicates from a list:**
my_list = [1, 2, 3, 2, 4, 1]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3, 4}

#* **Membership testing:**

my_set = {1, 2, 3}
if 2 in my_set:
  print("2 is in the set")
 
#* **Set operations:**

set1 = {1, 2, 3}
set2 = {2, 3, 4}
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4}