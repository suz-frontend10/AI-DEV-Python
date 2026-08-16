# Original lambda
process = lambda d: {
    k: (v * 2 if isinstance(v, int)
        else v.upper() if isinstance(v, str)
        else v)
    for k, v in d.items()
}

print(process({"a": 5, "b": "hi", "c": 3.5}))


# Rewritten using def
def process_dict(d):
    """
    Double integer values, convert string values to uppercase,
    and leave all other values unchanged.
    """

    result = {}

    for k, v in d.items():

        if isinstance(v, int):
            result[k] = v * 2

        elif isinstance(v, str):
            result[k] = v.upper()

        else:
            result[k] = v

    return result


print(process_dict({"a": 5, "b": "hi", "c": 3.5}))