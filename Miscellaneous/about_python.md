# Python Info

## Is Python pass-by-reference?
Yes, Python is pass by reference in all cases. The key point is that some objects are immutable and cannot be changed (ex. numeric types, strings, tuples). When we attempt to mutate them, a new object reference (with the updated value) is assigned to the variable instead. This is sometimes called **pass-by-assignment**.

Note: Python does not actually have traditional primitive types - they are all objects.

Source:
- https://www.quora.com/How-do-I-pass-a-variable-by-reference-in-Python/answer/Tony-Flury
