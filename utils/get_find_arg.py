def get_find_arg(filter_value: str) -> bool | None:
    """_summary_

    Args:
        filter_value (str): value of filter that got from  query string

    Returns:
        bool | None: True | False | None
    """
    if filter_value is "completed":
        return True
    if filter_value is "active":
        return False
    return None
