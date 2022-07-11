def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    for i in range(0, len(value)):
        if value[i] != value[-1-i]:
            return False
        else:
            return True
    # pass  # remove pass statement and implement me
