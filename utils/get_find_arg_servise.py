def get_find_arg(filter_value: str) -> bool | None:
    """Returns True, False or None depending for filter value that can be all, completed or active

    Args:
        filter_value (str): value of filter that got from  query string

    Returns:
        bool | None: True | False | None
    """
    if filter_value == "completed":
        return True
    if filter_value == "active":
        return False
    return None
