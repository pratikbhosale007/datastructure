## Why Dictionary Keys Must Be Immutable

#In Python, dictionary keys must be immutable data types. This means that they cannot be changed after they are created. While this might seem restrictive, it's essential for the proper functioning of dictionaries.

### Reasons for Immutability:

#1. **Hashing:** Dictionaries use hashing to efficiently store and retrieve key-value pairs. The hash value of a key is used to determine its location within the dictionary. If keys could be changed, their hash values would also change, making it impossible to find them using the original key.
#2. **Comparison:** When searching for a key in a dictionary, Python compares the hash value of the key being searched with the hash values of the keys in the dictionary. If keys were mutable, their hash values could change, leading to incorrect comparisons and potential data loss.
#3. **Consistency:** Immutable keys ensure that the dictionary remains consistent. If keys could be changed, it would be difficult to guarantee that the same key would always refer to the same value.

### Examples of Immutable Data Types:
#* **Numbers:** Integers, floats, and complex numbers are all immutable.
#* **Strings:** Strings are also immutable.
#* **Tuples:** Tuples are immutable collections of elements.

### Examples of Mutable Data Types That Cannot Be Used as Keys:
#* **Lists:** Lists are mutable, so they cannot be used as dictionary keys.
#* **Dictionaries:** Dictionaries are also mutable and cannot be used as keys.
#* **Sets:** Sets are mutable and cannot be used as keys.