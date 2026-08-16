def clean(text):
    return text.strip()

def to_lower(text):
    return text.lower()

def remove_spaces(text):
    return text.replace(" ", "_")

def add_prefix(text):
    return "user_" + text

def pipeline(text, *operations):

    print("Starting with:", repr(text))

    for operation in operations:

        text = operation(text)
        print("after", operation.__name__, ":", repr(text))

    print("Final:", text)

pipeline(
    "   Ravi Kumar Sharma   ",
    clean,
    to_lower,
    remove_spaces,
    add_prefix
)