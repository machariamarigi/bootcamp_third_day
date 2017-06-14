def find_max_min(number_list):
    """
        Function takes a list of integers as an argument and returns a list
        containing the minimum and maximum number
    """
    if not isinstance(number_list, list):
        raise TypeError("Function only accepts lists as valid argument")

    # List to hold minimum number and maximum number
    max_min_list = []

    if min(number_list) != max(number_list):
        max_min_list.append(min(number_list))
        max_min_list.append(max(number_list))
        return max_min_list
    elif min(number_list) == max(number_list):
        max_min_list.append(len(number_list))
        return max_min_list
