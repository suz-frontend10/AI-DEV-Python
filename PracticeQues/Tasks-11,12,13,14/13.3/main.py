import random

print(random.randint(1, 10))


# This is MY random file
# Traceback (most recent call last):
#   File "e:\Python_Dev_AI\Assignment-1\Task-13\13.3 The Name Collision Disaster\main.py", line 3, in <module>
#     print(random.randint(1, 10))
#           ^^^^^^^^^^^^^^
# AttributeError: module 'random' has no attribute 'randint' (consider renaming 


# When Python sees:
# import random it finds our local random.py instead of Python's built-in/standard-library random module.
# Our random.py doesn't contain: randint()
# so random.randint(1, 10) fails.

# How to fix it?
# As the question says:
# Delete your random.py file.
# Delete the __pycache__ folder created in that directory.
# Run main.py again.