
def str_len(str_in: str) -> str:
    """
    Given a string parameter, this function should return the length of the parameter.
    """
    return len(str_in)
    # pass  # remove pass statement and implement me


def first_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the first letter of the parameter.
    """
    return str_in[0]
    # pass  # remove pass statement and implement me


def last_char(str_in: str) -> str:
    """
    Given a string parameter, this function should return the last letter of the parameter..
    """
    return str_in[-1]
    # pass  # remove pass statement and implement me


def input_has_substring(str_in: str, sub_str_in: str) -> bool:
    """
    This function determines if the substring exists within the string. Returns True or False.
    """
    return str_in.__contains__(sub_str_in)
    # pass  # remove pass statement and implement me


def substring(str_in: str, start: int, stop: int) -> str:
    """
    Returns the substring of a string.

    Keyword arguments:
    str_in -- the string in which to generate a substring from
    start -- starting position of the input parameter to start the substring (inclusive)
    stop -- stopping position of the input parameter to stop the substring (exclusive)
    """
    return str_in[start:stop]
    # pass  # remove pass statement and implement me


def opposite_case(str_in: str) -> str:
    """
    Given a string parameter, this function returns the same string back with each letter having the opposite case.
    Example: 
    When input = "Python" the function returns "pYTHON"
    """

    return str_in.swapcase()
    # pass  # remove pass statement and implement me
