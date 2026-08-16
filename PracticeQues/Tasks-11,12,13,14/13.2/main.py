import stringtools as st

print(st.reverse("python"))
print(st.is_palindrome("madam"))
print(st.count_vowels("education"))
print(st.title_case("ravi kumar"))
print(st.remove_spaces("a b c"))

from stringtools import *

print("\nTesting __all__:")
print(reverse("python"))
if "_private_helper" in globals():
    print("_private_helper is available")
else:
    print("_private_helper is hidden")